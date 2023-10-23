from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    DEPARTMENT = (
        ('ENG', 'ENG'),
        ('FO', 'FO'),
        ('HK', 'HK'),
        ('FB', 'FB'),
        ('LUN', 'LUN'),
        ('IT', 'IT'),
    )

    department = models.CharField(max_length=50, choices= DEPARTMENT)
  

    def __str__(self):
        return self.username
