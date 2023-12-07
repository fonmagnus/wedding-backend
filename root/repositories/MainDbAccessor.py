from root.modules.main.models import *

class MainDbAccessor:
  def get_invitee(self, code) -> Invitee :
    if isinstance(code, Invitee):
      return code
    invitee = Invitee.objects.filter(code=code)
    if (not invitee.exists()):
      return None
    return invitee.first()
  
  def rsvp(self, code, request):
    invitee = self.get_invitee(code)
    invitee.quota = max(1, min(request.get('quota', 1), 10))
    invitee.is_attended = request.get('is_attended', False)
    invitee.save()
    self.send_message_to_bride(code, request)
    return invitee

  def send_message_to_bride(self, code, request) -> MessageToBride:
    invitee = self.get_invitee(code)
    message = request.get('message', '')
    message = MessageToBride.objects.update_or_create(
      defaults={
        'invitee': invitee,
        'message': message
      },
      invitee=invitee
    )
    return message
  
  def get_messages(self):
    return MessageToBride.objects.all().order_by('-updated_at')
  
  def get_activity(self, type):
    try:
      return Activity.objects.get(type=type)
    except Activity.DoesNotExist:
      return None
  
  def respond_activity(self, type, code, data):
    activity = self.get_activity(type)
    if activity == None:
      return 
    
    invitee = self.get_invitee(code)
    if invitee == None:
      return
    
    activity_response = self.get_activity_response(type, code)
    if activity_response is not None:
      return activity_response
    
    (activity_response, created) = ActivityResponse.objects.update_or_create(
      defaults={
        'invitee': invitee,
        'activity': activity,
        'response': self.sanitize_activity_response(data, type)
      },
      invitee=invitee,
      activity=activity
    )

    return activity_response
  
  def get_activity_response(self, type, code):
    try:
      response = ActivityResponse.objects.get(
        activity__type=type,
        invitee__code=code
      )
      return response
    except ActivityResponse.DoesNotExist:
      return None
  
  def sanitize_activity_response(self, data, type):
    if type == 'orange':
      return self.sanitize_orange(data)
    elif type == 'yellow':
      return self.sanitize_yellow(data)

  def sanitize_orange(self, data):
    responses = []
    slugs = [item.get('slug') for item in Activity.PropertyOrange.questions]
    answered_slugs = []
    for response in data.get('response'):
      slug = response.get('slug')
      if not slug in slugs or slug in answered_slugs:
        continue
      he_or_she = response.get('he_or_she')
      if he_or_she != 'he' and he_or_she != 'she':
        continue
      responses.append({
        'slug': slug,
        'he_or_she': he_or_she
      })
      answered_slugs.append(slug)
    return responses
  
  def sanitize_yellow(self, data):
    responses = []
    slugs = [item.get('slug') for item in Activity.PropertyYellow.questions]
    items = {
      item.get('slug'): {
        'EN': item.get('EN').get('options'),
        'ID': item.get('ID').get('options'),
      } for item in Activity.PropertyYellow.questions
    }
    
    lang = data.get('lang')
    
    answered_slugs = []
    for response in data.get('response'):
      slug = response.get('slug')
      answer = response.get('answer')
      
      if not slug in slugs or slug in answered_slugs:
        continue
      if not lang in ['EN', 'ID']:
        continue
      if not items.get(slug):
        continue
      if not answer in items.get(slug).get(lang):
        continue
      responses.append({
        'slug': slug,
        'lang': lang,
        'answer': answer
      })
      answered_slugs.append(slug)
    
    return responses
    