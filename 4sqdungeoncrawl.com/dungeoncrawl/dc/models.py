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
    ('all','All Attributes'),
]

# Create your models here.
class Player(models.Model):
    """Basic data universal to all players"""
    foursquare_id = models.CharField(max_length=200)
    access_token = models.TextField()
    last_checkin_time = models.DateTimeField(auto_now_add=True)

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
    image_url = models.CharField(max_length=100,blank=True)
    flavor_text = models.TextField(blank=True)
    effect = models.TextField(blank=True) # JSON encoding of effects
    value = models.IntegerField(blank=True,default=0)
    attribute_type = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)

class PlayerInventory(models.Model):
    """The player's inventory of items."""
    player = models.ForeignKey(Player)
    item_type = models.ForeignKey(ItemType)
    count = models.IntegerField()

class GiftBox(models.Model):
    """An item left by a specific player at a location for pickup by friends"""
    venue_id = models.CharField(max_length=100)
    item_type = models.ForeignKey(ItemType)
    count = models.IntegerField()

class MonsterType(models.Model):
    """Categories of monsters.

    This stores all the information needed to create a specific monster
    for a specific encounter."""
    name = models.CharField(max_length=100)
    image_url = models.CharField(max_length=100,blank=True)
    flavor_text = models.TextField(blank=True)
    min_level = models.IntegerField()
    max_level = models.IntegerField()
    attribute_type = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)

class CategoryAttribute(models.Model):
    foursquare_category = models.CharField(max_length=100)
    attribute_type = models.CharField(max_length=20, choices=ATTRIBUTE_CHOICES)

class Encounter(models.Model):
    """An Encounter is the event that happens after a player checks in to
    a given place. When we see a check in, we generate an encounter for
    that check in. The encounter
    """
    venue_id = models.CharField(max_length=100)
    monster_type = models.ForeignKey(MonsterType, null=True)
    monster_level = models.IntegerField(null=True)
    item_type = models.ForeignKey(ItemType, null=True)
    checkin_time = models.DateTimeField(auto_now_add=True)
