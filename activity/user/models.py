"""Model classes for user."""

from django.contrib.auth.models import User
from django.db import models

from user.choices import TimeZones


class Profile(models.Model):
    """User's profile information."""

    user = models.OneToOneField(User, related_name='profile',
                                on_delete=models.CASCADE)
    unique_id = models.CharField(max_length=200, blank=True, null=True, unique=True)
    real_name = models.CharField(max_length=200, blank=True, null=True)
    time_zone = models.CharField(max_length=4, choices=TimeZones.choices,
                                 default=TimeZones.AsiaKolkata)
    created_at = models.DateTimeField(auto_now=True)
    modified_at = models.DateTimeField(auto_now=True)

class ActivityPeriod(models.Model):
    """User activity information."""

    profile = models.ForeignKey(Profile, related_name='activityperiod',
                         on_delete=models.CASCADE)
    start_period = models.DateTimeField()
    end_period = models.DateTimeField()
