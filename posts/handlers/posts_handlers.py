import os

from comments.models import Comment
from posts.models import Post, UpvotePost, DownvotePost
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model

User = get_user_model()


class PostsHandler:

    def upvote(self, post: Post, user: User):
        user_upvote = UpvotePost.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            raise APIException("User already is upvoted")

        user_downvote = DownvotePost.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            user_downvote.delete()

        new_upvote = UpvotePost(user=user, post=post)
        new_upvote.save()

    def downvote(self, post: Post, user: User):
        user_downvote = DownvotePost.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            raise APIException("User already is downvoted")

        user_upvote = UpvotePost.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            user_upvote.delete()

        new_downvote = DownvotePost(user=user, post=post)
        new_downvote.save()

    def comments(self, post: Post):
        return Comment.objects.filter(post=post)
