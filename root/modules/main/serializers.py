from rest_framework import serializers
from .models import Invitee, MessageToBride

class InviteeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invitee
    fields = [
      'name',
      'code',
      'quota',
      'is_attended',
      'message_from_bride',
    ]

class InviteeNameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invitee
    fields = [
      'name',
    ]
  

class MessageSerializer(serializers.ModelSerializer):
  invitee = InviteeNameSerializer(many=False)
  class Meta:
    model = MessageToBride
    fields = [
      'invitee',
      'message'
    ]