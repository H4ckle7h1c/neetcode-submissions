class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Step 1 - find a candidate row that could contain the target
        for row in matrix:
            if row[0] == target:
                return True
            if row[-1] == target:
                return True   
            
            # Step 2 - We found a candidate row that could contain the target
            if row[0] < target and target < row[-1]:
                l, r = 0, len(row) - 1 
                while l < r:
                    mid = (r - l) // 2 + l 

                    if row[mid] == target:
                        return True

                    if row[mid] < target: 
                        l = mid + 1
                        continue
                    
                    if row[mid] > target: 
                        r = mid - 1
                        continue
                
                return False
        
        return False
                
        
        

        