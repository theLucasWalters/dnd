# imports
import functions as f
import rolls as r


# useful variables
## alignments
aligns = [
    "Lawful Good",
    "Neutral Good",
    "Chaotic Good",
    "Lawful Neutral",
    "True Neutral",
    "Chaotic Neutral",
    "Lawful Evil",
    "Neutral Evil",
    "Chaotic Evil",
]

## character classes
classes = [
    "barbarian",
    "bard",
    "cleric",
    "druid",
    "fighter",
    "monk",
    "paladin",
    "ranger",
    "rogue",
    "sorcerer",
    "warlock",
    "wizard"
]

## all the difference species
### I got this list from https://www.dndbeyond.com/races; it may not be complete
all_species = [
    "Human",
    "Dwarf",
    "Dragonborn",
    "Elf",
    "Gnome",
    "Half-Elf",
    "Halfling",
    "Half-Orc",
    "Tiefling",
    "Orc of Exandria",
    "Leonin",
    "Satyr",
    "Lineages",
    "Fairy",
    "Harengon",
    "Owlin",
    "Arakocra",
    "Genasi",
    "Goliath",
    "Aasimar",
    "Bugbear",
    "Firbolg",
    "Goblin",
    "Hobgoblin",
    "Kenku",
    "Kobold",
    "Lizardfolk",
    "Orc",
    "Tabaxi",
    "Triton",
    "Yuan-ti Pureblood",
    "Feral Tiefling",
    "Tortle",
    "Changeling",
    "Kalashtar",
    "Orc of Eberron",
    "Shifter",
    "Warforged",
    "Gith",
    "Centaur",
    "Loxodon",
    "Minotaur",
    "Simic Hybrid",
    "Vedalken",
    "Verdan",
    "Locathah",
    "Grung",
]

## all the different items a character can have
consumables = [
    "Dagger",
    # others to be added
]


# OBJECTS
## CHARACTERS
class Character(object):
    def __init__(self,
        name:str,
        hit_points:int,
        alignment:str,
        _class:str,
        level:int,
        species:str,
        strength:int,
        dexterity:int,
        constitution:int,
        intelligence:int,
        wisdom:int,
        charisma:int,
        equipment:list[str]=[]):

        self.name         = name
        self.hp           = hit_points
        self.alignment    = alignment
        self._class       = _class # use `_class` to not interfere with Python's `class` word
        self.level        = level
        self.species      = species
        self.equipment    = equipment
        self.check_valid()
        self.strength     = strength
        self.dexterity    = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom       = wisdom
        self.charisma     = charisma
        self.set_modifiers(strength, dexterity, constitution, intelligence, wisdom, charisma)
        self.initiative   = self.dex_mod

    # method to check if values input are valid
    def check_valid(self):
        error:bool = False

        if self.alignment not in aligns:
            print(Exception(f"Not a valid alignment: '{self.alignment}'"))
            error = True
        if self.species not in all_species:
            print(Exception(f"Not a valid species: '{self.species}'"))
            error = True
        if self._class not in classes:
            print(Exception(f"Not a valid class: '{self._class}'"))
            error = True

        if error:
            quit()

    def set_modifiers(self, stren, dex, const, intel, wis, charis):
        self.stren_mod  = f.set_mods(stren)
        self.dex_mod    = f.set_mods(dex)
        self.const_mod  = f.set_mods(const)
        self.intel_mod  = f.set_mods(intel)
        self.wis_mod    = f.set_mods(wis)
        self.charis_mod = f.set_mods(charis)


class Player(Character):
    def __init__(self, name, hit_points, alignment, level, species, equipment, friendly:bool=True):
        super().__init__(name, hit_points, alignment, level, species, equipment)
        self.friendly = friendly


class NPC(Character):
    def __init__(self, name, hit_points, alignment, level, species):
        super().__init__(name, hit_points, alignment, level, species)


class Friendly(NPC):
    def __init__(self, name, hit_points, alignment, level, species, equipment, friendly:bool=True):
        super().__init__(name, hit_points, alignment, level, species, equipment)
        self.friendly = friendly


class Enemy(NPC):
    def __init__(self, name, hit_points, alignment, level, species, equipment, friendly:bool=False):
        super().__init__(name, hit_points, alignment, level, species, equipment)
        self.friendly = friendly


## ITEMS
class Item:
    def __init__(self, price:float, weight:float):
        self.price  = price
        self.weight = weight


class Weapon(Item):
    def __init__(self, price, weight, damage:int):
        super().__init__(price, weight)
        self.damage = damage


class Consumable(Item):
    def __init__(self, price, weight, description:str):
        super().__init__(price, weight)
        self.description = description


# for testing
if __name__ == "__main__":
    name = "Markuss Kingston"
    race = all_species[0] # human
    char_class = classes[4] # fighter
    hp = r.creator_hp(char_class)
    test_character = Character
