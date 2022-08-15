from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from posts.handlers.posts_handlers import PostsHandler
from posts.models import Post
from posts.serializers.posts_serializers import PostSerializer
from soc_media.permissions import IsCreatorPermission


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsCreatorPermission]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def create(self, request, *args, **kwargs):
        print("erer")
        return super().create(request, *args, **kwargs)

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
