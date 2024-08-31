class Solution:
    def isValid(self, s: str) -> bool:

        opening = {
            '(': None,
            '[': None,
            '{': None,
            ')': '(',
            ']': '[',
            '}': '{',
        }

        stack = []
        for parenthesis in s:
            opening_parenthesis = opening[parenthesis]
            if opening_parenthesis is None:
                stack.insert(0, parenthesis)
            else:
                if len(stack) == 0:
                    return False
                elif opening_parenthesis == stack[0]:
                    stack.pop(0)
                else:
                    return False
        if stack:
            return False
        return True
