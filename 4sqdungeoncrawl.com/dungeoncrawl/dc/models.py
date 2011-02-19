from django.db import models

# Create your models here.
class Player(models.Model):
    """Basic data universal to all players"""


class ItemType(models.Model):
    """Categories for Items.

    Each item should contain an item type which handles all data
    commmon to any items of this type."""

class PlaceType(models.Model):
    """Categories for places.

    Each place is expected to have it's own type, which will store
    any important information universal to all places of that type"""
