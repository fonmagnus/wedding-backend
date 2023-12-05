from root.repositories.MainDbAccessor import MainDbAccessor

class MainService:
  def __init__(self):
    self.db_accessor = MainDbAccessor()

  def get_invitee(self, code):
    return self.db_accessor.get_invitee(code)
  
  def rsvp(self, code, request):
    return self.db_accessor.rsvp(code, request)
  
  def send_message_to_bride(self, code, request):
    return self.db_accessor.send_message_to_bride(code, request)
  
  def get_messages(self):
    return self.db_accessor.get_messages()