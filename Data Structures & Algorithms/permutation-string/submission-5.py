class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False 

        seen1=[0] * 26
        seen2=[0] * 26 
        
        for i in range(len(s1)):
            seen1[ord(s1[i]) - ord('a')] += 1
            seen2[ord(s2[i]) - ord('a')] += 1
        
        match_count = sum(seen1[i] == seen2[i] for i in range(len(seen1)) )
        
        if match_count == 26:
                return True

        for i in range(len(s1),len(s2)):
            # if new idx match = increment
            idx_r = ord(s2[i]) - ord('a')
            seen2[idx_r]+=1 
            if seen2[idx_r] == seen1[idx_r]:
                match_count+=1
            elif seen2[idx_r]-1 == seen1[idx_r]:
                match_count-=1

            # if old idx match = decrement
            idx_l = ord(s2[i- len(s1)]) - ord('a')
            seen2[idx_l] -= 1
            
            if seen2[idx_l] == seen1[idx_l]:
                match_count+=1
            elif seen2[idx_l]+1 == seen1[idx_l]:
                match_count-=1

            if match_count == 26:
                return True

        return False

         

        