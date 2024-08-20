from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    LIVE = 0
    DELETE = 1
    DELETE_CHOICES = (
        (LIVE, 'Live'),
        (DELETE, 'Delete')
    )

    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    name = models.CharField(max_length=255)
    mobile_no = models.CharField(max_length=12)
    status = models.IntegerField(choices=DELETE_CHOICES, default=LIVE)  # Optional: Add status field if needed
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)  # Optional: Add gender field if needed
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.user.username
