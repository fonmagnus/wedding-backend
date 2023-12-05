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