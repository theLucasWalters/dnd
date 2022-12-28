import random


# roll a d100
def d100() -> int:
    return random.randint(1, 100)


# roll a d20
def d20(character, modifier:str, advantage:bool=False, disadvantage:bool=False) -> int:
    raw_roll:int = random.randint(1, 20)
    final_roll:int = 0

    if (raw_roll == 1):
        # crit fail
        return 1
    elif (raw_roll == 20):
        # crit success
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


# roll a d12
def d12() -> int:
    return


# roll a d10
def d10() -> int:
    return


# roll a d8
def d8() -> int:
    return


# roll a d6
def d6() -> int:
    return


# roll a d4
def d4() -> int:
    return


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
