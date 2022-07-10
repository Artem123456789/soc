from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

from posts.handlers.posts_handlers import PostsHandler
from posts.models import Post
from posts.serializers.posts_serializers import PostSerializer
from posts.serializers.posts_serializers import VotePostInputSerializer, CommentInputSerializer
from posts.permissions import IsCreatorPermission


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsCreatorPermission]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

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

    @action(methods=["post"], detail=False, permission_classes=[permissions.IsAuthenticated])
    def comment(self, request):
        serializer = CommentInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        input_entity = serializer.save()

        PostsHandler().comment(input_entity, self.request.user)

        return Response(status=status.HTTP_201_CREATED)
