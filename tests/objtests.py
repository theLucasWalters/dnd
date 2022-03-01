from objects import *

player = Player(
    name = "Main",
    hit_points = 15,
    alignment = aligns[0],
    level = 1,
    skill = None,
    species = "Human",
    equipment = [
        consumables[0]
    ]
)

print(player.name)
print(player.hp)
print(player.alignment)
print(player.level)
print(player.skill)
print(player.species)
print(player.equipment)
