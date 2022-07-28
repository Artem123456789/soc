from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from chating.handlers.chating_handlers import ChatingHandler
from chating.serializers.chating_serializers import SendMessageInputSerializer, GetChatInputSerializer, \
    SentMessageSerializer


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def send_message(request):
    serializer = SendMessageInputSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    input_entity = serializer.save()

    ChatingHandler().send_message(input_entity, request.user)

    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def get_chat(request):
    serializer = GetChatInputSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    input_entity = serializer.save()

    response = ChatingHandler().get_chat(input_entity, request.user)

    return Response(SentMessageSerializer(response, many=True).data, status=status.HTTP_200_OK)
