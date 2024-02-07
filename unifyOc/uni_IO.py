import unifyOc.recUni as recUni

OPENING_PAR_ORG = ["(", "[", "{"]
CLOSING_PAR_ORG = [")", "]", "}"]
SEPERATORS = [","]
SEP_SP = [" "]


class InputError(Exception):

    msg: str

    def __int__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


def resolve_res_list(resolved_input: list, index_stack: list):
    """
    :param resolved_input: this is the list were input is parsed down into it
    :param index_stack: a stack is used to save the inner lists positions
    :return: return a reference to the current inner list to add, remove, etc
    """
    e = resolved_input

    for i in index_stack:
        e = e[i]

    return e


def parseInput(input_user: str):

    # the variables used to keep track of
    # opening and closing parenthesis
    open_par = 0
    close_par = 0

    # help to put the function name into its inter list
    # by saying weather the previous name was constant or
    # variable
    pre_name = False

    resolved_input = list()
    index_stack = list()

    for c in input_user:
        res_resolved_input = resolve_res_list(resolved_input, index_stack)

        if recUni.isConstant(c) or recUni.isVariable(c):
            pre_name = True
            res_resolved_input.append(c)

        elif c in OPENING_PAR_ORG:
            if pre_name:

                index_stack.append(len(res_resolved_input) - 1)
                pre = res_resolved_input.pop()
                res_resolved_input.append(list([pre]))
            else:
                index_stack.append(len(res_resolved_input))
                res_resolved_input.append(list([" "]))

            pre_name = False

            open_par += 1

        elif c in CLOSING_PAR_ORG:
            pre_name = False
            close_par += 1

            if len(index_stack) == 0:
                raise InputError("Parenthesis are used incorrectly")
            index_stack.pop()

        elif c in SEPERATORS:
            pre_name = False
            pass

        elif c in SEP_SP:
            pass

        else:
            print(c)
            raise InputError("Use of unknown character.")

    if open_par != close_par:
        raise InputError("Parenthesis are used incorrectly")

    return resolved_input


def printSubRules(subR: dict):
    """
    :param subR: substitution rules
    :return: prints the substitution rules using equal sign between variable
    and the value it is assigned to.
    """

    def printValue(value):

        if recUni.isFuncOListType(value):

            start = 0

            if recUni.isFunction(value):
                start = 1
                print(value[0], end="")

            last = False
            print("(", end="")

            for i in range(start, len(value), 1):
                printValue(value[i])

                if i == len(value) - 1:
                    last = True

                if not last:
                    print(",", end="")

            print(")", end="")
        else:
            print(value, end="")

    if len(subR) == 0:
        print("No subRules found!")
    else:
        for key in subR:
            print(key,"=", end='')
            printValue(subR[key])
            print()

