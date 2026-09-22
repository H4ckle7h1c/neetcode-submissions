class Solution:
    def isValid(self, s: str) -> bool:
        closingPairs = {
            '{': '}',
            '[': ']',
            '(': ')'
        }
        if len(s) % 2 != 0:
            return False

        stack = [] 
        for i in range(len(s)):
            if s[i] in closingPairs:
                stack.append(s[i])
                continue
            if not stack:
                return False
            last = stack.pop()
            if closingPairs[last] != s[i]:
                return False
        return len(stack) == 0