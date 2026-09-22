class Solution:
    def isValid(self, s: str) -> bool:
        matching_brackets = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        if len(s) % 2 != 0:
            return False

        stack = [] 
        for c in s:
            if c in matching_brackets:
                stack.append(c)
                continue
            if not stack:
                return False

            if matching_brackets[stack.pop()] != c:
                return False
        return len(stack) == 0