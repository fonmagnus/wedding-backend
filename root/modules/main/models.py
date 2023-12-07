from django.contrib.postgres.fields import JSONField
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
  

class Activity(BaseModel):
  class ActivityChoices(models.TextChoices):
    BLACK = 'black'
    RED = 'red'
    ORANGE = 'orange'
    YELLOW = 'yellow'
    GREEN = 'green'
    BLUE = 'blue'
    VIOLET = 'violet'
    PINK = 'pink'
    WHITE = 'white'
  
  type = models.CharField(max_length=256, choices=ActivityChoices.choices)
  content = models.JSONField(null=True, blank=True, default=dict)
  
  def __str__(self):
    return self.type

  class PropertyOrange:
    questions = [
      {
        'slug': 'who-is-the-more-responsible',
        'EN_text': 'Who is the more responsible one?',
        'ID_text': 'Siapa yang lebih bertanggung jawab?',
        'EN_adj': 'Responsible',
        'ID_adj': 'Tanggung Jawab'
      }, 
      {
        'slug': 'who-is-the-more-caring-one',
        'EN_text': 'Who is the more caring one?',
        'ID_text': 'Siapa yang lebih perhatian?',
        'EN_adj': 'Caring',
        'ID_adj': 'Perhatian'
      },
      {
        'slug': 'who-is-the-more-sarcastic',
        'EN_text': 'Who is the more sarcastic one?',
        'ID_text': 'Siapa yang lebih sarkas (suka menyindir)?',
        'EN_adj': 'Sarcastic',
        'ID_adj': 'Sarkas'
      }
    ]

class ActivityResponse(BaseModel):
  invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  response = models.JSONField(null=True, blank=True, default=dict)

  def __str__(self):
    return f'{self.activity} - {self.invitee}'