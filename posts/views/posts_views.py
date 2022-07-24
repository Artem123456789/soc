from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from comments.serializers.comments_serializers import CommentSerializer
from posts.handlers.posts_handlers import PostsHandler
from posts.models import Post
from posts.serializers.posts_serializers import PostSerializer
from posts.permissions import IsCreatorPermission


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsCreatorPermission]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    @action(methods=["post"], detail=False, permission_classes=[permissions.IsAuthenticated])
    def bearer_check(self, request, pk, *args, **kwargs):
        post = self.get_object()
        PostsHandler().upvote(post, self.request.user)

    @action(methods=["post"], detail=True, permission_classes=[permissions.IsAuthenticated])
    def upvote(self, request, pk, *args, **kwargs):
        post = self.get_object()
        PostsHandler().upvote(post, self.request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=True, permission_classes=[permissions.IsAuthenticated])
    def downvote(self, request, pk, *args, **kwargs):
        post = self.get_object()
        PostsHandler().downvote(post, self.request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["get"], detail=True)
    def comments(self, request, pk, *args, **kwargs):
        post = self.get_object()
        response = PostsHandler().comments(post)

        return Response(CommentSerializer(response, many=True).data, status=status.HTTP_200_OK)
