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
  
  def get_activity(self, type):
    return self.db_accessor.get_activity(type)
  
  def get_activity_response(self, type, code):
    return self.db_accessor.get_activity_response(type, code)
  
  def respond_activity(self, type, code, data):
    return self.db_accessor.respond_activity(type, code, data)