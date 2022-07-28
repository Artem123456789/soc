from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status

from chating.handlers.chating_handlers import ChatingHandler
from chating.serializers.chating_serializers import SendMessageInputSerializer


@api_view(["POST"])
@permission_classes([permissions.IsAuthenticated])
def send_message(request):
    serializer = SendMessageInputSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    input_entity = serializer.save()

    ChatingHandler().send_message(input_entity, request.user)

    return Response(status=status.HTTP_204_NO_CONTENT)
