

def isVariable(nameEntry: str):
    if isinstance(nameEntry, str):
        return nameEntry.isupper()
    return False


def isConstant(nameEntry: str):
    if isinstance(nameEntry, str):
        return nameEntry.islower()
    return False


def substitute(term1, term2):
    if isinstance(term2, list):
        return [substitute(term1, e) for e in term2]
    else:
        return term1.get(term2, term2)


def occur_check(variable, term):
    """
    Check if a variable occurs in a term.
    """
    if variable == term:
        return True
    elif isinstance(term, list):
        return any(occur_check(variable, sub_term) for sub_term in term)
    else:
        return False


class UnificationError(Exception):
    def __int__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


def unify(term1, term2):

    if (isConstant(term1) and isConstant(term2)) or (term1 == [] and term2 == []):
        if term1 == term2:
            return dict()
        raise UnificationError("Unification failed")

    elif isVariable(term1):
        #   occur check
        if occur_check(term1, term2):
            raise UnificationError
        return {term1: term2}

    elif isVariable(term2):
        #   occur check
        if occur_check(term2, term1):
            raise UnificationError
        return {term2: term1}

    elif len(term1) != len(term2) or len(term1) == 0 or len(term2) == 0:
        raise UnificationError("Unification failed")

    else:
        b1 = unify(term1[0], term2[0])

        TE1 = [substitute(b1, e) for e in term1[1:]]
        TE2 = [substitute(b1, e) for e in term2[1:]]
        b2 = unify(TE1, TE2)

        b1.update(b2)
        return b1


E1 = ["f", ["f", "X", "Y"], "X"]
E2 = ["f", ["f", "V", "U"], ["g", "U", "Y"]]

try:
    subRules = unify(E1, E2)
except UnificationError:
    print("Unification Error.")
else:
    print(subRules)

