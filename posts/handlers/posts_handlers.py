import os

from posts.models import Post


class PostsHandler:

    def delete_image(self, post_id: int):
        image_path = Post.objects.get(id=post_id).image.path
        os.remove(image_path)
