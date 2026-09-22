class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        box_index = lambda row, col: (row // 3) * 3 + (col // 3)
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = {}

        # Step 1: Validate rows
        for i in range(9):
            for j in range(9):

                if board[i][j] == '.':
                    continue

                if board[i][j] in rows[i]:
                    return False

                rows[i].add(board[i][j])

        print('Rows validated')

        # Step 2: Validate columns
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                if board[i][j] in cols[j]:
                    return False
                cols[j].add(board[i][j])
        print('Cols validated')
        # Step 3: Validate the sub boxes
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue

                idx = box_index(i,j)

                if idx not in boxes:
                    boxes[idx] = set()

                box = boxes[idx]
                if board[i][j] in box:
                    return False

                boxes[idx].add(board[i][j])
        print('Boxes validated')
        return True