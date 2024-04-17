from rest_framework import serializers
from .models import Invitee, MessageToBride, Activity, ActivityResponse, FriendGroup

class FriendGroupSerializer(serializers.ModelSerializer):
  class Meta:
    model = FriendGroup
    fields = [
      'name',
      'photo_order'
    ]

class InviteeSerializer(serializers.ModelSerializer):
  friend_group = FriendGroupSerializer(many=False)
  class Meta:
    model = Invitee
    fields = [
      'name',
      'code',
      'quota',
      'is_attended',
      'message_from_bride',
      'friend_group'
    ]

class InviteeNameSerializer(serializers.ModelSerializer):
  class Meta:
    model = Invitee
    fields = [
      'name',
      'is_attended'
    ]
  

class MessageSerializer(serializers.ModelSerializer):
  invitee = InviteeNameSerializer(many=False)
  class Meta:
    model = MessageToBride
    fields = [
      'invitee',
      'message'
    ]

class ActivitySerializer(serializers.ModelSerializer):
  class Meta:
    model = Activity
    fields = [
      'type', 'content'
    ]

class ActivityResponseSerializer(serializers.ModelSerializer):
  class Meta:
    model = ActivityResponse
    fields = [
      'response'
    ]