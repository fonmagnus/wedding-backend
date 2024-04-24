# Python
from django.core.management.base import BaseCommand, CommandError
import warnings

class Command(BaseCommand):
    help = 'RSVP management command'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        warnings.filterwarnings("ignore")  # Ignore warnings

        from django.db.models import Sum
        from root.modules.main.models import Invitee

        # Filter Invitee where is_attended is True
        attended_invitees = Invitee.objects.filter(is_attended=True)

        # Sum the quota
        total_quota = attended_invitees.aggregate(Sum('quota'))

        # total_quota is a dictionary like {'quota__sum': value}
        quota_sum = total_quota['quota__sum']
        self.stdout.write(str(quota_sum))  # Convert quota_sum to string