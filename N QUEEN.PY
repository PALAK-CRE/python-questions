class Solution:
    def solveNQueens(self, n: int):
        result = []
        
        # create board with '.'
        board = [["."] * n for _ in range(n)]

        def isSafe(board, row, col):
            # check column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False

            # check left diagonal
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1

            # check right diagonal
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1

            return True

        def helperFunction(board, row):
            if row == n:
                # convert each row to string
                temp = ["".join(r) for r in board]
                result.append(temp)
                return

            for col in range(n):
                if isSafe(board, row, col):
                    board[row][col] = 'Q'
                    helperFunction(board, row + 1)
                    board[row][col] = '.'   # backtrack

        helperFunction(board, 0)
        return result