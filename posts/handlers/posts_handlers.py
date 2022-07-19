import os

from comments.models import Comment
from posts.models import Post, Upvote, Downvote
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model

User = get_user_model()


class PostsHandler:

    def upvote(self, post: Post, user: User):
        user_upvote = Upvote.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            raise APIException("User already is upvoted")

        user_downvote = Downvote.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            user_downvote.delete()

        new_upvote = Upvote(user=user, post=post)
        new_upvote.save()

    def downvote(self, post: Post, user: User):
        user_downvote = Downvote.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            raise APIException("User already is downvoted")

        user_upvote = Upvote.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            user_upvote.delete()

        new_downvote = Downvote(user=user, post=post)
        new_downvote.save()

    def comments(self, post: Post):
        return Comment.objects.filter(post=post)
