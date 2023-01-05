import random

# valid types for d20 rolls
roll_types = [
    "attack",
    "check",
    "save"
]


# roll a d100
def d100() -> int:
    return random.randint(1, 100)


# roll a d20
# this is hands-down the most complex die rolling function
def d20(character, modifier:str, roll_type:str, advantage:bool=False, disadvantage:bool=False) -> int:
    # make sure the `roll_type` is valid
    if (roll_type not in roll_types):
        print(Exception(f"Not a valid roll type: '{roll_type}'")); quit()

    # get the raw roll
    raw_roll:int = random.randint(1, 20)

    if (raw_roll == 1):
        # crit fail
        return 1
    elif (raw_roll == 20):
        # crit success
        return 20
    elif (raw_roll == 19 and character._class == "fighter" and character.level == 3 and roll_type == "attack"):
        # level 3 fighters crit on attack rolls of 20 and 19
        return 20
    else:
        # add the necessary modifiers to the roll
        match modifier:
            case "strength":
                return raw_roll + character.stren_mod
            case "dexterity":
                return raw_roll + character.dex_mod
            case "constitution":
                return raw_roll + character.const_mod
            case "intelligence":
                return raw_roll + character.intel_mod
            case "wisdom":
                return raw_roll + character.wis_mod
            case "charisma":
                return raw_roll + character.charis_mod
            case "initiative":
                return raw_roll + character.initiative
            case "acrobatics":
                pass
            case "animal handling":
                pass
            case "arcana":
                pass
            case "athletics":
                pass
            case "deception":
                pass
            case "history":
                pass
            case "insight":
                pass
            case "intimidation":
                pass
            case "investigation":
                pass
            case "medicine":
                pass
            case "nature":
                pass
            case "perception":
                pass
            case "performance":
                pass
            case "persuasion":
                pass
            case "religion":
                pass
            case "sleight of hand":
                pass
            case "stealth":
                pass
            case "survival":
                pass


# determine characteristics for a new character
def creator_d20():
    # nothing quite yet
    return


# find out hp
def creator_hp(char_class):
    match char_class:
        case "barbarian":
            return d12()
        case "paladin":
            return d10()
        case "fighter":
            return d10()
        case "ranger":
            return d10()
        case "monk":
            return d8()
        case "druid":
            return d8()
        case "rogue":
            return d8()
        case "bard":
            return d8()
        case "cleric":
            return d8()
        case "warlock":
            return d8()
        case "wizard":
            return d6()
        case "sorcerer":
            return d6()


# roll a d12
def d12() -> int:
    return random.randint(1, 12)


# roll a d10
def d10() -> int:
    return random.randint(1, 10)


# roll a d8
def d8() -> int:
    return random.randint(1, 8)


# roll a d6
def d6() -> int:
    return random.randint(1, 6)


# roll a d4
def d4() -> int:
    return random.randint(1, 4)


# for testing only
if __name__ == "__main__":
    func:str = input("Enter the function you want > ")

    # PLEASE READ BEFORE RUNNING
    ## make sure to input a function's necessary parameters before testing
    match func:
        case "d100":
            d100()
        case "d20":
            d20()
        case "d12":
            d12()
        case "d10":
            d10()
        case "d8":
            d8()
        case "d6":
            d6()
        case "d4":
            d4()
