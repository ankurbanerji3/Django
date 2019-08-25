from django.db import models
from django.contrib.auth.models import User



class User_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    is_active = models.BooleanField(default=False)
    points = models.IntegerField(default=0)
    won = models.IntegerField(default=0)
    lost = models.IntegerField(default=0)
    drawn = models.IntegerField(default=0)
    college = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=20, default="")
