from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    def __str__(self):
        return self.header

    header = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to="post_images/", default=None)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
