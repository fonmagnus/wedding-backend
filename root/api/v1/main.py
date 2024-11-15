from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from django.http import JsonResponse

from root.services import main_service
from root.modules.main.serializers import InviteeSerializer, MessageSerializer, ActivitySerializer, ActivityResponseSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def get_invitee(request, code):
    invitee = main_service.get_invitee(code)
    serializer = InviteeSerializer(invitee, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["POST"])
@permission_classes([AllowAny])
def rsvp(request, code):
    invitee = main_service.rsvp(code, request.data)
    serializer = InviteeSerializer(invitee, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["POST"])
@permission_classes([AllowAny])
def send_message_to_bride(request, code):
    main_service.send_message_to_bride(code, request.data)
    return JsonResponse(
        data={
          'success': True
        },
        safe=False,
        status=200
    )

@api_view(["GET"])
@permission_classes([AllowAny])
def get_messages(request):
    messages = main_service.get_messages()
    serializer = MessageSerializer(messages, many=True)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["GET"])
@permission_classes([AllowAny])
def get_activity(request, type):
    activity = main_service.get_activity(type)
    serializer = ActivitySerializer(activity, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["GET"])
@permission_classes([AllowAny])
def get_activity_response(request, type, code):
    activity_response = main_service.get_activity_response(type, code)
    serializer = ActivityResponseSerializer(activity_response, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["POST"])
@permission_classes([AllowAny])
def respond_activity(request, type, code):
    response = main_service.respond_activity(type, code, request.data)
    serializer = ActivityResponseSerializer(response, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["GET"])
@permission_classes([AllowAny])
def get_loves(request):
    loves = main_service.get_loves()
    return JsonResponse(
        data={
            'loves': loves,
        },
        safe=False,
        status=200
    )

@api_view(["POST"])
@permission_classes([AllowAny])
def send_loves(request, code):
    loves = main_service.send_loves(code)
    return JsonResponse(
        data={
            'loves': loves,
        },
        safe=False,
        status=200
   )

@api_view(["POST"])
@permission_classes([AllowAny])
def open_invitation(request, code):
    invitee = main_service.open_invitation(code)
    serializer = InviteeSerializer(invitee, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )

@api_view(["POST"])
@permission_classes([AllowAny])
def register_invitee(request):
    invitee = main_service.register_invitee(request.data)
    serializer = InviteeSerializer(invitee, many=False)
    return JsonResponse(
        data=serializer.data,
        safe=False,
        status=200
    )