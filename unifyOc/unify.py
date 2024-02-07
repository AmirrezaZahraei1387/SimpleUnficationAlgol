import unifyOc.recUni as recUni


class UnificationError(Exception):

    msg: str

    def __int__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


def apply_substitution(subR, term):
    """
    :param subR: subRule we are going to apply on the term
    :param term: unification term
    :return: return the term while correct substitutions
    are made according to rules
    """

    if recUni.isFuncOListType(term):

        return [apply_substitution(subR, e) for e in term]
    else:
        return subR.get(term, term)


def occur_check(variable, term):
    """
    :param variable: unification variable used to check it
    in the term
    :param term: unification term
    :return: returns true if the term contains the variable, false
    otherwise.
    """
    if variable == term:
        return True
    elif recUni.isFuncOListType(term):
        return any(occur_check(variable, sub_term) for sub_term in term)
    else:
        return False


def unify_with_occur_check(term1, term2):

    if (recUni.isConstant(term1, True) and recUni.isConstant(term2, True)) or (term1 == [] and term2 == []):
        # if they are constant both or empty both they must equal
        if term1 == term2:
            return dict()
        raise UnificationError("Constant terms or functions are not equal.")

    elif recUni.isVariable(term1):
        #   occur check
        if occur_check(term1, term2):
            raise UnificationError("There are cycle between variable and its supposed value.")
        return {term1: term2}

    elif recUni.isVariable(term2):
        #   occur check
        if occur_check(term2, term1):
            raise UnificationError("There are cycle between variable and its supposed value.")
        return {term2: term1}

    elif len(term1) != len(term2) or len(term1) == 0 or len(term2) == 0:
        raise UnificationError("the number of elements in list or function parameter "
                               "does not match or there dependency cycles.")

    else:
        b1 = unify_with_occur_check(term1[0], term2[0])

        TE1 = [apply_substitution(b1, e) for e in term1[1:]]
        TE2 = [apply_substitution(b1, e) for e in term2[1:]]

        b2 = unify_with_occur_check(TE1, TE2)

        b1.update(b2)

        return b1

