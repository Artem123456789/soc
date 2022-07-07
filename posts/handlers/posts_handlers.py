import os

from posts.models import Post
from posts.serializers.posts_serializers import VotePostInputEntity


class PostsHandler:

    def delete_image(self, post_id: int):
        image_path = Post.objects.get(id=post_id).image.path
        os.remove(image_path)

    def upvote(self, input_entity: VotePostInputEntity):
        pass
