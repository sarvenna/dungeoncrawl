from django.db import models

ATTRIBUTE_CHOICES = [
    ('culture', 'Cultured'),
    ('fun', 'Fun'),
    ('food', 'Foodie'),
    ('hip', 'Hipster'),
    ('shop', 'Shopaholic'),
    ('fashion', 'Fashionista'),
    ('travel', 'Jet Setter'),
    ('mta', 'Commuter'),
    ('outdoor', 'Outdoorsy'),
    ('zen', 'Zen'),
    ('party', 'Party Animal'),
    ('bar', 'Alcoholic'),
    ('smart', 'Smart'),
    ('college', 'Collegiate'),
]

# Create your models here.
class Player(models.Model):
    """Basic data universal to all players"""
    foursquare_id = models.TextField()
    access_token = models.TextField()

class PlayerAttributes(models.Model):
    """The player's attributes. Statistics used in combat etc."""
    player = models.ForeignKey(Player)
    attribute_type = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)
    value = models.IntegerField()

class ItemType(models.Model):
    """Categories for Items.

    Each item should contain an item type which handles all data
    commmon to any items of this type."""
    name = models.CharField(max_length=100)
    flavor_text = models.TextField()
    effect = models.TextField() # JSON encoding of effects
    value = models.IntegerField()
    attribute_type = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)

class PlayerInventory(models.Model):
    """The player's inventory of items."""
    player = models.ForeignKey(Player)
    item_type = models.ForeignKey(ItemType)
    count = models.IntegerField()

class MonsterType(models.Model):
    """Categories of monsters.

    This stores all the information needed to create a specific monster
    for a specific encounter."""
    name = models.CharField(max_length=100)
    flavor_text = models.TextField()
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    attribute_type = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)


class PlaceType(models.Model):
    """Categories for places.

    Each place is expected to have it's own type, which will store
    any important information universal to all places of that type"""


class Encounter(models.Model):
    """An Encounter is the event that happens after a player checks in to
    a given place. When we see a check in, we generate an encounter for
    that check in. The encounter
    """
