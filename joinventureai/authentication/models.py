from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    # Add custom fields here if needed
    pass

    class Meta:
        # This prevents the clash with auth.User
        swappable = 'AUTH_USER_MODEL'


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_subscribed = models.BooleanField(default=False)