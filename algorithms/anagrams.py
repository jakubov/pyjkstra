class AnagramDetector:
    """ Two different ways to determine if two strings are anagrams """

    def is_anagram_one(self, first, second):
        """ Count characters and compare """
        first_map = dict()
        second_map = dict()

        for c in first:
            if c in first_map.keys():
                first_map[c] += 1
            else:
                first_map[c] = 1

        for c in second:
            if c in second_map.keys():
                second_map[c] += 1
            else:
                second_map[c] = 1

        for k in first_map.keys():
            if first_map.get(k) != second_map.get(k):
                return False

        return True

    def is_anagram_two(self, first, second):
        """ Sort strings and compare """
        first_list = list(first)
        second_list = list(second)

        first_list.sort()
        second_list.sort()

        for i in range(len(first_list)):
            if first_list[i] != second_list[i]:
                return False

        return True
