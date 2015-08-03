import unittest

from pyjkstra.data_structures.stack import Stack

class StackTestCase(unittest.TestCase):
    def setUp(self):
        """ Init the Stack """
        self.s = Stack()

    def tearDown(self):
        """ Empty the Stack """
        self.s = []

    def test_is_empty(self):
        """ Test Empty Stack """
        self.s = Stack()
        self.assertTrue(self.s.is_empty())

    def test_size(self):
        """ Test Stack Size """
        self.s.push("One")
        self.assertEquals(self.s.size(), 1)

        self.s.push("Two")
        self.s.push("Three")
        self.assertEquals(self.s.size(), 3)

    def test_push(self):
        """ Test Push """
        self.s.push("One")
        self.s.push("Two")
        self.s.push("Three")

        self.assertEquals(self.s.size(), 3)
        self.assertEquals(self.s[0], "One")
        self.assertEquals(self.s[1], "Two")
        self.assertEquals(self.s[2], "Three")

    def test_peek(self):
        """ Test Peek """
        self.s.push("One")
        self.assertEquals(self.s.peek(), "One")
        self.assertEquals(self.s.size(), 1)

        self.s.push("Two")
        self.s.push("Three")
        self.assertEquals(self.s.peek(), "Three")
        self.assertEquals(self.s.size(), 3)

    def test_pop(self):
        """ Test Pop """
        self.s.push("One")
        self.assertEquals(self.s.pop(), "One")
        self.assertEquals(self.s.size(), 0)

        self.s.push("Two")
        self.s.push("Three")
        self.assertEquals(self.s.pop(), "Three")
        self.assertEquals(self.s.size(), 1)
        self.assertEquals(self.s.pop(), "Two")
        self.assertEquals(self.s.size(), 0)
