import unittest
import unifyOc


class UnifyOccurCheckTest(unittest.TestCase):

    def test_unify_with_occur_check_correctNess(self):
        """
        tests the unify_with_occur_check with one several input
        to see its correctness
        """

        INPUT = [
            [['p', 'X', ['f', 'Y', 'Z']], ['p', 'a', ['f', 'b', 'c']]],
            [['f', 'X', ['g', 'Y']], ['f', 'a', ['g', 'b']]],
            [['p', ['f', 'X'], 'Y'], ['p', ['f', 'a'], 'b']],
            [['f', 'X', ['g', 'Y', 'Z']], ['f', 'a', ['g', 'b', 'c']]],
            [['p', ['f', 'X'], ['g', 'Y', 'Z']], ['p', ['f', 'a'], ['g', 'b', 'c']]],
            [['f', 'X', ['g', ['h', 'Y', 'Z']], 'W'], ['f', 'a', ['g', ['h', 'b', 'c']], 'd']],
            [['p', ['f', 'X', 'Y'], ['q', ['g', 'Z'], 'W']], ['p', ['f', 'a', 'b'], ['q', ['g', 'c'], 'd']]],
            [['f', ['g', 'X', ['h', 'Y']], ['i', 'Z', 'W']], ['f', ['g', 'a', ['h', 'b']], ['i', 'c', 'd']]],
            [['p', 'X', ['q', ['f', 'Y', 'Z'], 'W']], ['p', 'a', ['q', ['f', 'b', 'c'], 'd']]],
            [['f', 'X', ['g', 'Y', ['h', 'Z']], 'W'], ['f', 'a', ['g', 'b', ['h', 'c']], 'd']],
            [['f', 'X', ['g', ['h', 'Y', ['i', 'Z', ['j', 'W']]]], ['k', 'V']], ['f', 'a', ['g', ['h', 'b', ['i', 'c', ['j', 'd']]]], ['k', 'e']]],
            [['p', ['q', ['r', 'X', ['s', 'Y']], ['t', 'Z']], ['u', ['v', 'W'], ['w', 'V']]], ['p', ['q', ['r', 'a', ['s', 'b']], ['t', 'c']], ['u', ['v', 'd'], ['w', 'e']]]],
            [['f', ['g', 'X', ['h', 'Y', ['i', 'Z', ['j', 'W']]]], ['k', 'V'], ['l', 'U']], ['f', ['g', 'a', ['h', 'b', ['i', 'c', ['j', 'd']]]], ['k', 'e'], ['l', 'f']]],
            [['p', 'X', ['q', ['r', 'Y', ['s', 'Z', ['t', 'W']]], ['u', 'V']]], ['p', 'a', ['q', ['r', 'b', ['s', 'c', ['t', 'd']]], ['u', 'e']]]],
            [['f', 'X', ['g', 'Y', ['h', 'Z', ['i', 'W', ['j', 'V', ['k', 'U']]]]], ['l', 'T']], ['f', 'a', ['g', 'b', ['h', 'c', ['i', 'd', ['j', 'e', ['k', 'f']]]]], ['l', 'g']]],
            [['f', 'X', ['g', 'Y', ['h', 'Z', ['i', 'W', ['j', 'V']]]], ['l', 'T']], ['f', ['t', 'm', 'n'], ['g', 'b', ['h', ['f', 'c', 'i', ['g', 'w', 'w']], ['i', 'd', ['j', ['f', 'c', ['t', 'm', 'n']]]]]], ['l', 'g']]]
        ]

        for pair in INPUT:
            print(pair)
            result = unifyOc.unify_with_occur_check(pair[0], pair[1])
            print("sub is", result)
            self.assertEqual(unifyOc.apply_substitution(result, pair[0]), pair[1], "The substitution rule"
                                                                                   " does not work.")


if __name__ == "__main__":
    unittest.main()
