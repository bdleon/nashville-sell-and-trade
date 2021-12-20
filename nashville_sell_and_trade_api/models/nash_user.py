from django.db import models
from django.contrib.auth.models import User



class NashUser(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    picture = models.CharField(max_length=300)
