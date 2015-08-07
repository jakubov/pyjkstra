
class LinkedList:
    def __init__(self):
        """ Init the list """
        self.head = None
        self.size = 0

    def add(self, item):
        """ Add item to the list """
        raise NotImplementedError

    def remove(self, item):
        """ Remove the first occurence of item in list  """
        raise NotImplementedError

    def search(self, item):
        """ Search item in the list """
        raise NotImplementedError

    def is_empty(self):
        """ Return True if list empty, False otherwise """
        raise NotImplementedError

    def size(self):
        """ Return the size of the list """
        raise NotImplementedError
