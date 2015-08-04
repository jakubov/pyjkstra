import unittest

from pyjkstra.algorithms.anagrams import AnagramDetector

detector = AnagramDetector()

VALID_ANAGRAMS = [
    ('', ''),
    ('a', 'a'),
    ('ab', 'ab'),
    ('heart', 'earth'),
    ('python', 'typhon'),
    ('apple', 'pleap'),
    ('abcd', 'dcba'),
    ('112233', '123123'),
]

INVALID_ANAGRAMS = [
    (' ', 'a'),
    ('a', 'b'),
    ('heart', 'eerth'),
    ('python', 'tyfhon'),
    ('apple', 'pleep'),
    ('abcd', 'abcda'),
    ('112233', '123423'),
]


class AnagramTestCase(unittest.TestCase):

    def test_is_anagram_one(self):
        for pair in VALID_ANAGRAMS:
            self.assertTrue(detector.is_anagram_one(pair[0], pair[1]))

        for pair in INVALID_ANAGRAMS:
            self.assertFalse(detector.is_anagram_one(pair[0], pair[1]))

    def test_is_anagram_two(self):
        for pair in VALID_ANAGRAMS:
            self.assertTrue(detector.is_anagram_two(pair[0], pair[1]))

        for pair in INVALID_ANAGRAMS:
            self.assertFalse(detector.is_anagram_two(pair[0], pair[1]))
