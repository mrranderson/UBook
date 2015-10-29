from django.db import models
from django.contrib.auth.models import User

class UBookProfile(models.Model):
    user = models.OneToOneField(User)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zipcode = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

