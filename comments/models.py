from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(max_length=1000, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)

    @property
    def upvotes(self):
        return len(CommentUpvote.objects.filter(comment=self))

    @property
    def downvotes(self):
        return len(CommentDownvote.objects.filter(comment=self))


class CommentUpvote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class CommentDownvote(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
