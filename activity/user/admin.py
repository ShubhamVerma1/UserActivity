from django.contrib import admin

from user.models import (
    Profile,
    ActivityPeriod
)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""
    pass

@admin.register(ActivityPeriod)
class ActivityPeriodAdmin(admin.ModelAdmin):
    """Activity period admin."""
    pass
