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
  
  class PropertyYellow:
    questions = [
      {
        'slug': 'meet-up',
        'EN': {
          'text': 'Where did Arnold and Gaby first Met?',
          'options': [
            'Henshin Kuningan',
            'White Cafe',
            'The Breeze BSD',
            'Ropang Plus Plus Muara Karang'
          ],
          'fact': 'Arnold and Gaby first met in White Cafe, Gading Serpong',
          'correct_answer': 'White Cafe'
        },
        'ID': {
          'text': 'Dimana pertama kali Arnold dan Gaby bertemu?',
          'options': [
            'Henshin Kuningan',
            'White Cafe',
            'The Breeze BSD',
            'Ropang Plus Plus Muara Karang'
          ],
          'fact': 'Arnold dan Gaby pertama kali bertemu di White Cafe, Gading Serpong',
          'correct_answer': 'White Cafe'
        }
      },

      {
        'slug': 'favorite-food',
        'EN': {
          'text': "What is Gaby's favorite food?",
          'options': [
            'Pizza',
            'Chicken Soup',
            'Sushi',
            'Soto'
          ],
          'fact': 'Sushi 🍣 is Gaby\'s favorite food. We often go to Sushi Hiro because we find it delicious',
          'correct_answer': 'Sushi'
        },
        'ID': {
          'text': 'Apa makanan favorit Gaby?',
          'options': [
            'Pizza',
            'Sup Ayam',
            'Sushi',
            'Soto'
          ],
          'fact': 'Sushi 🍣 adalah makanan kesukaan Gaby. Kami sering pergi ke Sushi Hiro karena rasa sushinya yang enak',
          'correct_answer': 'Sushi'
        }
      },

      {
        'slug': 'relationship',
        'EN': {
          'text': 'How long Arnold and Gaby have been in a relationship until the wedding day?',
          'options': [
            '0 - 1 years',
            '1 - 2 years',
            '2 - 3 years',
            '3 - 4 years'
          ],
          'correct_answer': '2 - 3 years',
          'fact': 'Our relationship starts at 7th of May 2021. So it\'s been around 2-3 years we date each other before we marry'
        },
        'ID': {
          'text': 'Berapa lama Arnold dan Gaby berpacaran sebelum hari pernikahan kami?',
          'options': [
            '0 - 1 tahun',
            '1 - 2 tahun',
            '2 - 3 tahun',
            '3 - 4 tahun'
          ],
          'correct_answer': '2 - 3 tahun',
          'fact': 'Masa pacaran kami dimulai dari tanggal 7 Mei 2021. Sehingga sudah sekitar 2-3 tahun kami berpacaran sebelum menikah'
        }
      },

      {
        'slug': 'doll',
        'EN': {
          'text': 'Arnold and Gaby loves dolls. Which one of these dolls are NOT the animal doll we have?',
          'options': [
            'Panda',
            'Shark',
            'Dog',
            'Teddy Bear'
          ],
          'correct_answer': 'Teddy Bear',
          'fact': 'Gaby has a Panda and a Dog doll. While Arnold has a shark and a Rilakkuma doll. Although Rilakkuma is a bear, it is not a teddy bear'
        },
        'ID': {
          'text': 'Arnold dan Gaby suka boneka. Boneka manakah yang BUKAN milik kami?',
          'options': [
            'Panda',
            'Ikan Hiu',
            'Anjing',
            'Beruang Teddy'
          ],
          'correct_answer': 'Beruang Teddy',
          'fact': 'Gaby punya boneka panda dan anjing. Sementara Arnold punya boneka hiu dan Rilakkuma. Meskipun Rilakkuma adalah beruang, ia bukanlah teddy bear'
        }
      }
    ]

class ActivityResponse(BaseModel):
  invitee = models.ForeignKey(Invitee, on_delete=models.CASCADE)
  activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
  response = models.JSONField(null=True, blank=True, default=dict)

  def __str__(self):
    return f'{self.activity} - {self.invitee}'