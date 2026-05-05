from django.contrib.auth.models import AbstractUser
from django.db import models
from organizations.models import Organization


class User(AbstractUser):
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="users",
        null=True,
        blank=True
    )

    role = models.CharField(
        max_length=20,
        choices=[
            ('ADMIN', 'Admin'),
            ('MANAGER', 'Manager'),
            ('USER', 'User')
        ],
        default='USER'
    )

    def __str__(self):
        return self.username