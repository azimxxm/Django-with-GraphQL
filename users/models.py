from django.db import models
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin

class ExtendUser(AbstractUser):
    email = models.EmailField(blank=False, max_length=255, verbose_name="email")
    USERNAME_FIELD = "username"
    EMAIL_FIELD = "email"
