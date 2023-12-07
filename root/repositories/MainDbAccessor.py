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
  
  def sanitize_activity_response(self, data, type):
    if type == 'orange':
      return self.sanitize_orange(data)

  def sanitize_orange(self, data):
    responses = []
    slugs = [item.get('slug') for item in Activity.PropertyOrange.questions]
    for response in data.get('response'):
      slug = response.get('slug')
      if not slug in slugs:
        continue
      he_or_she = response.get('he_or_she')
      if he_or_she != 'he' and he_or_she != 'she':
        continue
      responses.append({
        'slug': slug,
        'he_or_she': he_or_she
      })
    return responses
    