from django.db import models
from django.contrib.auth import get_user_model

from posts.models import Post

User = get_user_model()


class Comment(models.Model):
    text = models.TextField(max_length=1000, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True)
