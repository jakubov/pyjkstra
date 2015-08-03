import unittest

from pyjkstra.data_structures.queue import Queue

class QueueTestCase(unittest.TestCase):

    def setUp(self):
        """ Init the Queue """

        self.q = Queue()

    def tearDown(self):
        """ Empty the Queue """

        self.q = []

    def test_is_empty(self):
        """ Test Empty Queue """

        self.assertTrue(self.q.is_empty())

    def test_is_not_empty(self):
        """ Test Non-Empty Queue """

        self.q.enqueue(1)
        self.assertFalse(self.q.is_empty())

    def test_size(self):
        """ Test Queue Size """

        self.assertEquals(self.q.size(), 0)

        self.q.enqueue("One")
        self.assertEquals(self.q.size(), 1)

        self.q.enqueue("Two")
        self.assertEquals(self.q.size(), 2)

        self.q.enqueue("Three")
        self.assertEquals(self.q.size(), 3)

        self.q.dequeue()
        self.q.dequeue()
        self.assertEquals(self.q.size(), 1)

        self.q.enqueue("wow")
        self.assertEquals(self.q.size(), 2)

    def test_enqueue(self):
        """ Test Enqueue """

        self.q.enqueue("One")
        self.assertEquals(self.q.size(), 1)
        self.assertFalse(self.q.is_empty())

        self.q.enqueue("Two")
        self.q.enqueue("Three")
        self.assertEquals(self.q.size(), 3)

    def test_dequeue(self):
        """ Test Dequeue """

        self.q.enqueue("One")
        self.q.enqueue("Two")
        self.q.enqueue("Three")
        self.assertEquals(self.q.size(), 3)

        self.q.dequeue()
        self.assertEquals(self.q.size(), 2)

        self.q.dequeue()
        self.assertEquals(self.q.size(), 1)

        self.q.dequeue()
        self.assertEquals(self.q.size(), 0)
        self.assertTrue(self.q.is_empty())
