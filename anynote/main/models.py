from django.db import models
from django.contrib.auth.models import AbstractUser
from jsonfield import JSONField
import collections

class User(AbstractUser):
    pass

class NoteModel(models.Model):
    """
    Contain info about a certain note
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    json_data = JSONField(load_kwargs = {'object_pairs_hook': collections.OrderedDict})
    hash = models.TextField()