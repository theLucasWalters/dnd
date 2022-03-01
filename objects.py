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

## all the difference species
### I got this list from https://www.dndbeyond.com/races; it may not be complete
species = [
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
]

# OBJECTS

## CHARACTERS
class Character(object):
    def __init__(self, name:str, hit_points:int, alignment:str, level:int, skill:str, species:str, equipment:str=[]):
        self.name       = name
        self.hp         = hit_points
        self.alignment  = alignment
        self.level      = level
        self.skill      = skill
        self.species    = species
        self.equipment  = equipment

class Player(Character):
    def __init__(self, name, hit_points, alignment, level, skill, species, equipment, friendly:bool=True):
        super().__init__(name, hit_points, alignment, level, skill, species, equipment)
        self.friendly = friendly

class NPC(Character):
    def __init__(self, name, hit_points, alignment, level, skill, species):
        super().__init__(name, hit_points, alignment, level, skill, species)

class Friendly(NPC):
    def __init__(self, name, hit_points, alignment, level, skill, species, equipment, friendly:bool=True):
        super().__init__(name, hit_points, alignment, level, skill, species, equipment)
        self.friendly = friendly

class Enemy(NPC):
    def __init__(self, name, hit_points, alignment, level, skill, species, equipment, friendly:bool=False):
        super().__init__(name, hit_points, alignment, level, skill, species, equipment)
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
