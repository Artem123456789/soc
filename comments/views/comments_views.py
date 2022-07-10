from rest_framework import viewsets
from rest_framework import permissions

from comments.models import Comment
from comments.serializers.comments_serializers import CommentSerializer


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]
