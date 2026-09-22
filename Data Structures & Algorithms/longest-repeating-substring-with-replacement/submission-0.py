class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        l = 0
        max_length = 0 
        max_count = 0

        for r in range(len(s)):
            seen[s[r]] = seen.get(s[r], 0) + 1
            
            max_count = max(max_count, seen[s[r]])

            while (r - l + 1) - max_count > k:
                seen[s[l]] -= 1
                l += 1

            max_length = max(max_length, r - l + 1)

        return max_length

