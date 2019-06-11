from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    mobile_no = models.IntegerField()

    def __str__(self):
        return self.user.username


class Crops(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return '%s ' % (self.name)
