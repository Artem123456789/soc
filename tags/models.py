from django.db import models

from tags.constants import TAG_MAX_LEN


class Tag(models.Model):
    text = models.CharField(max_length=TAG_MAX_LEN, null=True, blank=True)
