from django.db import models

# Create your models here.
class Player(models.Model):
    """Basic data universal to all players"""
    foursquare_id = models.TextField()
    access_token = models.TextField()

class PlayerAttributes(models.Model):
    """The player's attributes. Statistics used in combat etc."""
    player = models.ForiegnKey(Player)
    cultured = models.IntegerField()
    fun = models.IntegerField()
    foodie = models.IntegerField()
    hipster = models.IntegerField()
    shopaholic = models.IntegerField()
    fashionista = models.IntegerField()
    jet_setter = models.IntegerField()
    commuter = models.IntegerField()
    outdoorsy = models.IntegerField()
    zen = models.IntegerField()
    party_animal = models.IntegerField()
    alcoholic = models.IntegerField()
    hard_working = models.IntegerField()
    healthy = models.IntegerField()
    smart = models.IntegerField()
    collegiate = models.IntegerField()

class ItemType(models.Model):
    """Categories for Items.

    Each item should contain an item type which handles all data
    commmon to any items of this type."""
    name = models.CharField(max_length=100)
    flavor_text = models.TextField()
    effect = models.TextField() # JSON encoding of effects 

class PlayerInventory(models.Model):
    """The player's inventory of items."""
    player = models.ForiegnKey(Player)
    item_type = models.ForiegnKey(ItemType)
    count = models.IntegerField()

class PlaceType(models.Model):
    """Categories for places.

    Each place is expected to have it's own type, which will store
    any important information universal to all places of that type"""


class Encounter(models.Model):
    """An Encounter is the event that happens after a player checks in to
    a given place. When we see a check in, we generate an encounter for
    that check in. The encounter
    """
