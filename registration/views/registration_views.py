from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from registration.serializers.registration_serializers import RegisterInputSerializer, RegisterResponseSerializer
from registration.handlers.registration_handlers import RegistrationHandler


@api_view(["POST"])
def register(request):
    serializer = RegisterInputSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)

    input_entity = serializer.save()
    response = RegistrationHandler().register(input_entity)

    return Response(RegisterResponseSerializer(response).data, status=status.HTTP_201_CREATED)
