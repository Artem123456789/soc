from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from posts.handlers.posts_handlers import PostsHandler
from posts.models import Post
from posts.serializers.posts_serializers import PostSerializer
from posts.serializers.posts_serializers import VotePostInputSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def update(self, request, *args, **kwargs):
        PostsHandler().delete_image(int(kwargs.get("pk")))
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        PostsHandler().delete_image(int(kwargs.get("pk")))
        return super().destroy(request, *args, **kwargs)

    @action(methods=["post"], detail=False, permission_classes=[permissions.IsAuthenticated])
    def upvote(self, request):
        serializer = VotePostInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()

        PostsHandler().upvote(input_entity.post_id, self.request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)

    @action(methods=["post"], detail=False, permission_classes=[permissions.IsAuthenticated])
    def downvote(self, request):
        serializer = VotePostInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()

        PostsHandler().downvote(input_entity.post_id, self.request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)
