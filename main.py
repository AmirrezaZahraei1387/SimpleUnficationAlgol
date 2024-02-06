import unifyOc
import sys


def main():

    DESCRIPTION = """Important: Please make sure you use low letters for 
constants, and functions and upper case for variables\n"""
    print(DESCRIPTION)

    exp1 = input("Please enter the expression: ")

    try:
        exp1 = unifyOc.parseInput(exp1)
    except unifyOc.InputError:
        print(sys.exc_info()[1])
        sys.exit(1)

    print("Expression 1 captured successfully!\n")

    exp2 = input("Please enter the expression: ")
    try:
        exp2 = unifyOc.parseInput(exp2)
    except unifyOc.InputError:
        print(sys.exc_info()[1])
        sys.exit(1)

    print("Expression 2 captured successfully!\n")

    print("start unification ...")
    try:
        unify_result = unifyOc.unify_with_occur_check(exp1, exp2)
    except unifyOc.UnificationError:
        print(sys.exc_info()[1])
        sys.exit(1)

    print("substitution rules are:")
    unifyOc.printSubRules(unify_result)


if __name__ == "__main__":
    main()






