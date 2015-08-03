from pyjkstra.data_structures.stack import Stack


class BalancedParentheses:

    def is_balanced(self, word):
        stack = Stack()
        balanced = True
        for c in word:
            if c == '(':
                stack.push(c)
            else:
                if stack.is_empty():
                    balanced = False
                else:
                    stack.pop()

        return balanced and stack.is_empty()
