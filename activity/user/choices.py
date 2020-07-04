from django.db import models

class TimeZones(models.TextChoices):
    """Class for time zones mapping."""

    AsiaKolkata = '1', 'Asia/Kolkata'
    AmericaLosAngeles = '2', 'America/Los_Angeles'
    AmericaCreston = '3', 'America/Creston'
    AsiaKathmandu = '4', 'Asia/Kathmandu'
