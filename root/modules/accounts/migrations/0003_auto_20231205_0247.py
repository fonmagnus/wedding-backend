# Generated by Django 3.1 on 2023-12-05 02:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20220818_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='deleted_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='experience',
            name='deleted_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='profile',
            name='deleted_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='deleted_at',
            field=models.DateTimeField(default=None, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='socialmediaaccount',
            name='is_deleted',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]