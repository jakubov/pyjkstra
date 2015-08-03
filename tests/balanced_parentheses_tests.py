import unittest

from pyjkstra.algorithms.balanced_parentheses import BalancedParentheses


BALANCED_STRINGS = [
    '()',
    '((()))',
    '(()()()())',
    '(()((())()))',
    '(()((())()))()()'
]

UNBALANCED_STRINGS = [
    '(',
    ')(',
    '()))',
    '(()()(()',
    '((((((((())'
]

bp = BalancedParentheses()


class BalancedParenthesesTestCase(unittest.TestCase):

    def test_is_balanced(self):
        for s in BALANCED_STRINGS:
            self.assertTrue(bp.is_balanced(s))

        for s in UNBALANCED_STRINGS:
            self.assertFalse(bp.is_balanced(s))
