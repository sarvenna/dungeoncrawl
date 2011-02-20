import random

from dc.models import Encounter, ItemType, MonsterType

class EncounterGenerator():
    """Class for generating random encounters. Mostly a kinda static nonsense
    class, but it's handy for organizing stuff
    """
    MONSTER_CHANCE = 50
    JUNK_CHANCE = 80

    def generate_encounter(foursquare_id, venue_id, venue_category, checkin_time):
        """Generates an encounter for the player for checking in to the given
        venue at the given time."""
        # Roll to see if the player gets an item or a monster
        encounter_roll = random.randint(1,100)
        if encounter_roll < MONSTER_CHANCE:
            # It's a monster!
            a = None
        else:
            # Give the player an item!
            item_roll = random.randint(1,100)
            if item_roll < JUNK_CHANCE:
                # Give the player a junk item
                a = None
            else:
                # Give the player a real item
                
