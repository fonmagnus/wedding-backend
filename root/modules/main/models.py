from django.db import models
from root.modules.generic.models import BaseModel
import random, string

# Create your models here.
class Invitee(BaseModel):
  name = models.CharField(max_length=512, db_index=True)
  code = models.CharField(max_length=256, db_index=True, editable=False)
  quota = models.IntegerField(default=1)
  is_attended = models.BooleanField(default=False)
  message_from_bride = models.TextField(null=True, blank=True)

  def random_alphanumeric_string(self, length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for i in range(length))
  
  def __str__(self):
    return f'{self.name} - {self.code}'

  def save(self):
    if self.code == None or len(self.code) == 0:
      self.code = self.random_alphanumeric_string(9)

    super().save()


class MessageToBride(BaseModel):
  invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  message = models.TextField()

  def __str__(self):
    return f'Message from {self.invitee.name}'