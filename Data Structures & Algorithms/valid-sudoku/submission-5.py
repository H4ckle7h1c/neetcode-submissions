class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        sq_index = lambda row, col: ((row // 3) , (col // 3))
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue
                isInvalid = val in rows[r] or val in cols[c] or val in squares[sq_index(r,c)]
                if isInvalid: 
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[sq_index(r,c)].add(val)
        return True