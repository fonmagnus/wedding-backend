# Generated by Django 3.1 on 2023-12-05 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_invitee_message_from_bride'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invitee',
            name='message_from_bride',
            field=models.TextField(blank=True, null=True),
        ),
    ]
