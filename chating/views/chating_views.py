from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action


class ChatingViewSet(viewsets.GenericViewSet):
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=["post"], detail=False)
    def send_message(self, request):
        return