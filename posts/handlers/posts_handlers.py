import os

from posts.models import Post, Upvote, Downvote
from posts.serializers.posts_serializers import VotePostInputEntity
from django.contrib.auth import get_user_model

User = get_user_model()


class PostsHandler:

    def delete_image(self, post_id: int):
        image_path = Post.objects.get(id=post_id).image.path
        os.remove(image_path)

    def upvote(self, post_id: int, user: User):
        post = Post.objects.get(id=post_id)
        user_upvote = Upvote.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            raise Exception("User already is upvoted")

        user_downvote = Downvote.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            user_downvote.delete()

        new_upvote = Upvote(user=user, post=post)
        new_upvote.save()

    def downvote(self, post_id: int, user: User):
        post = Post.objects.get(id=post_id)
        user_downvote = Downvote.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            raise Exception("User already is downvoted")

        user_upvote = Upvote.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            user_upvote.delete()

        new_downvote = Downvote(user=user, post=post)
        new_downvote.save()
