# Generated by Django 4.2.9 on 2024-04-09 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_alter_love_invitee'),
    ]

    operations = [
        migrations.AddField(
            model_name='invitee',
            name='opened_invitation_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
