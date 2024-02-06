

def isVariable(nameEntry: str):
    if isinstance(nameEntry, str):
        return nameEntry[0].isupper()
    return False


def isConstant(nameEntry: str):
    if isinstance(nameEntry, str):
        return nameEntry[0].islower()
    return False


def isFuncOListType(nameEntry: list):
    return isinstance(nameEntry, list)


def isFunction(nameEntry: list):
    if isinstance(nameEntry, list) and len(nameEntry) != 0:
        return nameEntry[0] != " "
    return False


def isList(nameEntry: list):
    if isinstance(nameEntry, list) and len(nameEntry) != 0:
        return nameEntry[0] == " "
    return False

