class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seenS1 = [0 for x in range(26)]
        seenS2 = [0 for x in range(26)]
        l = 0
        
        for c in s1:
            seenS1[ord(c) % 26] += 1 

        for r in range(len(s2)):
            seenS2[ord(s2[r]) % 26] += 1

            if r - l + 1 == len(s1):
                if seenS1 == seenS2:
                    return True
                seenS2[ord(s2[l]) % 26 ] -= 1
                l+=1
        return False
