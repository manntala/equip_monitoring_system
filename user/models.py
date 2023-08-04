from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from model_utils.models import TimeStampedModel
from company.models import Company, Department
from equipment.models import Equipment

from user import Gender


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)
    

class User(AbstractBaseUser, TimeStampedModel):
    email = models.EmailField(unique=True)
    first_name = models.CharField(blank=False, max_length=100)
    middle_name = models.CharField(blank=False, max_length=100)
    last_name = models.CharField(blank=False, max_length=100)
    gender = models.CharField(choices=Gender.CHOICES, max_length=10)
    contact_number = models.CharField(max_length=50, null=True)
    
    employee_number = models.CharField(max_length=20, blank=True)
    job_title = models.CharField(max_length=50, blank=True)

    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="users", null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="users", null=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE, related_name="users", null=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"
    

