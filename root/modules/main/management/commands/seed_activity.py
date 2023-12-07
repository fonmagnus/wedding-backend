from typing import Any
from django.core.management.base import BaseCommand, CommandError, CommandParser
from root.modules.main.models import Activity

class Command(BaseCommand):
  help = 'Seed activity'

  def add_arguments(self, parser):
    pass
  
  def handle(self, *args, **options):
    self.init_orange()
    self.init_yellow()
    self.stdout.write(self.style.SUCCESS('Successfully seeded activity'))
    pass

  def init_orange(self):
    questions = Activity.PropertyOrange.questions

    Activity.objects.update_or_create(
      defaults={
        'type': Activity.ActivityChoices.ORANGE,
        'content': questions
      },
      type=Activity.ActivityChoices.ORANGE
    )
      
  def init_yellow(self):
    questions = Activity.PropertyYellow.questions
    Activity.objects.update_or_create(
      defaults={
        'type': Activity.ActivityChoices.YELLOW,
        'content': questions
      },
      type=Activity.ActivityChoices.YELLOW
    )
