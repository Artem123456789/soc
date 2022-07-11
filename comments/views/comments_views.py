from rest_framework import viewsets
from rest_framework import permissions

from comments.models import Comment
from comments.serializers.comments_serializers import CommentSerializer
from comments.permissions import IsCreatorPermission


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCreatorPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
