from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from comments.handlers.comments_handler import CommentsHandler
from comments.models import Comment
from comments.serializers.comments_serializers import CommentSerializer
from comments.permissions import IsCreatorPermission


class CommentsViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsCreatorPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(methods=["post"], detail=True, permission_classes=[IsAuthenticated])
    def upvote(self, request, pk, *args, **kwargs):
        comment = self.get_object()
        CommentsHandler().upvote(comment, request.user)

        return Response(status=status.HTTP_201_CREATED)

    @action(methods=["post"], detail=True, permission_classes=[IsAuthenticated])
    def downvote(self, request, pk, *args, **kwargs):
        comment = self.get_object()
        CommentsHandler().downvote(comment, request.user)

        return Response(status=status.HTTP_201_CREATED)
