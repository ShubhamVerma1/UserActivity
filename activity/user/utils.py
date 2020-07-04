"""Utils for user."""

from random import randint

from user.factories import (
    ActivityPeriodFactory,
    ProfileFactory
)


def create_dummy_activity_periods():
    """Create dummy activity period."""
    profile = ProfileFactory()

    for i in range(randint(1, 4)):
        ActivityPeriodFactory(
            profile=profile
        )
