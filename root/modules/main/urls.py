# ./bookstore_app/api/urls.py

from django.urls import include, path
from root.api.v1 import main

urlpatterns = [
    path('me/<str:code>', main.get_invitee),
    path('rsvp/<str:code>', main.rsvp),
    path('say/<str:code>', main.send_message_to_bride),
    path('messages', main.get_messages)
]
