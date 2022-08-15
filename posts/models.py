from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Post(models.Model):
    def __str__(self):
        return self.header

    header = models.CharField(max_length=200, null=True, blank=True)
    text = models.TextField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    @property
    def upvotes(self):
        return len(UpvotePost.objects.filter(post=self))

    @property
    def downvotes(self):
        return len(DownvotePost.objects.filter(post=self))

    @property
    def images(self):
        return PostImage.objects.filter(post=self)


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to="post_images/", null=True, blank=True)


class UpvotePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)


class DownvotePost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
