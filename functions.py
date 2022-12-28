import errors as err

def set_mods(attrib):
    if (attrib == 1):
        return -5
    elif (attrib == 2 or attrib == 3):
        return -4
    elif (attrib == 4 or attrib == 5):
        return -3
    elif (attrib == 6 or attrib == 7):
        return -2
    elif (attrib == 8 or attrib == 9):
        return -1
    elif (attrib == 10 or attrib == 11):
        return 0
    elif (attrib == 12 or attrib == 13):
        return 1
    elif (attrib == 14 or attrib == 15):
        return 2
    elif (attrib == 16 or attrib == 17):
        return 3
    elif (attrib == 18 or attrib == 19):
        return 4
    elif (attrib == 20 or attrib == 21):
        return 5
    elif (attrib == 22 or attrib == 23):
        return 6
    elif (attrib == 24 or attrib == 25):
        return 7
    elif (attrib == 26 or attrib == 27):
        return 8
    elif (attrib == 28 or attrib == 29):
        return 9
    elif (attrib == 30):
        return 10
    else: print(Exception(f"Invalid attribute value: \"{attrib}\"")); quit()

# for testing only
if __name__ == "__main__":
    test:int = set_mods(20)
    print(test)
