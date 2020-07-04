"""Factory for user app models."""

import datetime
import pytz
from random import randint, choice

import string

from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User

from factory import Faker, LazyAttribute, Sequence, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyDateTime, FuzzyText

from user.choices import TimeZones
from user.models import (
    ActivityPeriod,
    Profile
)


class ProfileFactory(DjangoModelFactory):
    """Profile objects factory."""

    class Meta:
        """Meta Class."""

        model = Profile

    user = SubFactory('user.factories.UserFactory')
    real_name = Faker('name')
    unique_id = FuzzyText(length=8,
                   chars=string.ascii_uppercase + string.digits, prefix='W0')
    time_zone = choice(TimeZones.values)


class UserFactory(DjangoModelFactory):
    """User objects factors factory."""

    class Meta:
        """Meta Class."""

        model = User

    email = FuzzyText(length=4, suffix='@abc.com')
    username = FuzzyText(length=4)
    password = make_password('password')


class ActivityPeriodFactory(DjangoModelFactory):
    """Activity Period factory."""

    class Meta:
        """Meta Class."""

        model = ActivityPeriod

    profile = SubFactory('user.factories.ProfileFactory')
    start_period = FuzzyDateTime(
        datetime.datetime(2020, 5, 1, tzinfo=pytz.UTC),
        datetime.datetime(2020, 5, 5, tzinfo=pytz.UTC)
    )
    end_period = FuzzyDateTime(
        datetime.datetime(2020, 5, 6, tzinfo=pytz.UTC),
        datetime.datetime(2020, 5, 10, tzinfo=pytz.UTC)
    )
