class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Step 1 - find a candidate row that could contain the target with binary search
        lower, upper = 0, len(matrix) - 1

        while lower <= upper:
            midMatrix = (upper - lower) // 2 + lower

            if matrix[midMatrix][0] > target:
                upper = midMatrix - 1

            if matrix[midMatrix][-1] < target:
                lower = midMatrix + 1

            # Step 2 - We found a candidate row that could contain the target
            if matrix[midMatrix][0] <= target and target <= matrix[midMatrix][-1]:
                l, r = 0, len(matrix[midMatrix]) - 1 
                while l <= r:
                    mid = (r - l) // 2 + l 

                    if matrix[midMatrix][mid] == target:
                        return True

                    if matrix[midMatrix][mid] < target: 
                        l = mid + 1
                        continue
                    
                    if matrix[midMatrix][mid] > target: 
                        r = mid - 1
                        continue
                
                return False
        
        return False
                
        
        

        