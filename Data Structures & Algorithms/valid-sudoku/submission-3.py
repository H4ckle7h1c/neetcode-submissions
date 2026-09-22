class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_index = lambda row, col: (row // 3) * 3 + (col // 3)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        for r in range(9):          
            for c in range(9):
                val = board[r][c]
                
                if val == '.':
                    continue

                idx = box_index(r,c)

                if idx not in boxes:
                    boxes[idx] = set()

                if val in rows[r]:
                    return False

                if val in cols[c]:
                    return False

                if val in boxes[idx]:
                    return False

            
                rows[r].add(val)
                cols[c].add(val)
                boxes[idx].add(val)

        return True