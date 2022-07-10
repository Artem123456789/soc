import os

from posts.models import Post, Upvote, Downvote, Comment
from posts.entities.posts_entites import CommentInputEntity
from rest_framework.exceptions import APIException
from django.contrib.auth import get_user_model

User = get_user_model()


class PostsHandler:

    def upvote(self, post_id: int, user: User):
        post = Post.objects.get(id=post_id)
        user_upvote = Upvote.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            raise APIException("User already is upvoted")

        user_downvote = Downvote.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            user_downvote.delete()

        new_upvote = Upvote(user=user, post=post)
        new_upvote.save()

    def downvote(self, post_id: int, user: User):
        post = Post.objects.get(id=post_id)
        user_downvote = Downvote.objects.filter(user=user, post=post)
        if len(user_downvote) > 0:
            raise APIException("User already is downvoted")

        user_upvote = Upvote.objects.filter(user=user, post=post)
        if len(user_upvote) > 0:
            user_upvote.delete()

        new_downvote = Downvote(user=user, post=post)
        new_downvote.save()

    def comment(self, input_entity: CommentInputEntity, user: User):
        comment = Comment(text=input_entity.text,
                          post=Post.objects.get(id=input_entity.post_id),
                          user=user)
        comment.save()
