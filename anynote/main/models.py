from django.contrib.auth.models import User
from django.db import models


class NoteModel(models.Model):
    """Note Model
    """

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.JSONField(default=dict)
    hash = models.CharField(max_length=200, default="")

