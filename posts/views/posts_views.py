from rest_framework import viewsets

from posts.handlers.posts_handlers import PostsHandler
from posts.models import Post
from posts.serializers.posts_serializers import PostSerializer


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
