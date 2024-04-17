# ./bookstore_app/api/urls.py

from django.urls import include, path
from root.api.v1 import main

urlpatterns = [
    path('me/<str:code>', main.get_invitee),
    path('rsvp/<str:code>', main.rsvp),
    path('say/<str:code>', main.send_message_to_bride),
    path('messages', main.get_messages),
    path('activity/<str:type>', main.get_activity),
    path('activity-response/<str:type>/<str:code>', main.get_activity_response),
    path('respond-activity/<str:type>/<str:code>', main.respond_activity),
    path('get-loves', main.get_loves),
    path('send-loves/<str:code>', main.send_loves),
    path('open-invitation/<str:code>', main.open_invitation),
    path('register-invitee', main.register_invitee),
]
