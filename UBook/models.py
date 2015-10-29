from django.db import models
from django.contrib.auth.models import User

class UBookProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=255)

