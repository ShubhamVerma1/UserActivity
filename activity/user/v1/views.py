"""Views for user api."""

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

import arrow

from collections import defaultdict

from user.choices import TimeZones
from user.models import (
    ActivityPeriod,
    Profile
)


class UserActivityView(APIView):
    """View for sending all user activity."""

    def get_all_activity_data_for_profile(self, profile, timezone):
        """Return formatted activity data for a profile."""
        all_user_activities = ActivityPeriod.objects.filter(profile=profile)
        activity_data = []

        for activity in all_user_activities:
            activity_data.append({
                'start_time': arrow.get(activity.start_period).to(
                    timezone).strftime('%b %-d %Y  %-I:%M%p'
                ),
                'end_time': arrow.get(activity.end_period).to(
                    timezone).strftime('%b %-d %Y  %-I:%M%p'
                )
            })

        return activity_data

    def perpare_data(self):
        """Prepare data."""
        all_profiles = Profile.objects.all()
        data_collection = []
        for profile in all_profiles:
            timezone = TimeZones(profile.time_zone).label
            activity_data = self.get_all_activity_data_for_profile(
                profile, timezone)
            if activity_data:
                data_collection.append(
                    {
                        'id': profile.unique_id,
                        'real_name': profile.real_name,
                        'tz': timezone,
                        'activity_periods': activity_data
                    }
                )
        return data_collection

    def get(self, request):
        """Get all details of users and their activity."""
        return Response(
            data= {
                'ok': True,
                'members': self.perpare_data()
            },
            status=status.HTTP_200_OK
        )
