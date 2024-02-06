
def isVariable(nameEntry: str):
    if isinstance(nameEntry, str):
        return nameEntry[0].isupper()
    return False


def isConstant(nameEntry: str):
    if isinstance(nameEntry, str):
        return nameEntry[0].islower()
    return False


def isFuncOList(nameEntry: list):
    return isinstance(nameEntry, list)
