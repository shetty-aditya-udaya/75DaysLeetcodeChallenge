class Solution:
    def totalNQueens(self, n: int) -> int:
        count = 0
        board = [-1] * n

        def backtrack(row):
            nonlocal count

            if row == n:
                count += 1
                return

            for col in range(n):
                if is_safe(row, col):
                    board[row] = col
                    backtrack(row + 1)
                    board[row] = -1

        def is_safe(row, col):
            for prev_row in range(row):
                prev_col = board[prev_row]

                # Same column
                if prev_col == col:
                    return False

                # Same diagonal
                if abs(prev_row - row) == abs(prev_col - col):
                    return False

            return True

        backtrack(0)
        return count