from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
import datetime

class Request(models.Model):
    DEPARTMENT = (
        ('ENG', 'ENG'),
        ('FO', 'FO'),
        ('HK', 'HK'),
        ('FB', 'FB'),
        ('LUN', 'LUN'),
        ('IT', 'IT'),
    )

    STATUS = (
        ('Pending', 'Pending'),
        ('Done', 'Done'),
    )
    room = models.CharField(max_length=50)
    department = models.CharField(max_length=50, choices= DEPARTMENT)
    request = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices= STATUS, default='Pending')
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.room

    @property
    def diff(self):
        tu = self.date_updated
        to = self.date_added
        diff = tu - to
        return diff.total_seconds() / 60

    def get_absolute_url(self):
        return reverse("main:update", kwargs={"pk": self.pk})