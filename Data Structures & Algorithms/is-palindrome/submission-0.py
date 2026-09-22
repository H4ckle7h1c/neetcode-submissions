class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0 
        newS = ''.join(c.lower() for c in s if c.isalnum())
        right = len(newS) - 1

        while left < right:
            if newS[left] != newS[right]: 
                return False
            left += 1
            right -= 1 
        return True