from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Custom User model for Home WiFi Security application."""
    class Meta:
        db_table = 'custom_user'
