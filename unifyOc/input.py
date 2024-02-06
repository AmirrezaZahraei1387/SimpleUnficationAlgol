import unifyOc.recUni as recUni

OPENING_PAR_ORG = ["(", "[", "{"]
CLOSING_PAR_ORG = [")", "]", "}"]
SEPERATORS = [","]
SEP_SP = [" "]


class InputError(Exception):
    def __int__(self, msg):
        self.msg = msg
        super().__init__(self.msg)


def resolve_res_list(resolved_input: list, index_stack: list):

    e = resolved_input

    for i in index_stack:
        e = e[i]

    return e


def parseInput(input_user: str):

    open_par = 0
    close_par = 0
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
                index_stack.append(len(res_resolved_input) - 1)
                res_resolved_input.append(list())

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


