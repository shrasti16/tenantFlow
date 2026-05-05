from django.db import models

class Organization(models.Model):
    name = models.CharField(max_length=255)
    domain = models.CharField(max_length=255, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name