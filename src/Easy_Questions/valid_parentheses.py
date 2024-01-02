class Solution:
    def isValid(self, s: str) -> bool:
        parentheses = {'(': ')', '[': ']', '{': '}'}
        left_stack = []

        for char in s:
            if char in parentheses.keys():
                left_stack.append(char)
            else:
                if len(left_stack) == 0:
                    return False
                left_parenthesis = left_stack.pop()
                if parentheses[left_parenthesis] != char:
                    return False

        return True if len(left_stack) == 0 else False


