class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0] * n for _ in range(n)]
        self.solution = []

    def solve(self):
        if self.solve_backtracking(0):
            self.print_solution()
        else:
            print("No solution found!")

    def solve_backtracking(self, col):
        if col >= self.n:
            return True

        for row in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                if self.solve_backtracking(col + 1):
                    return True
                self.board[row][col] = 0

        return False

    def is_safe(self, row, col):
        for c in range(col):
            if self.board[row][c] == 1:
                return False
            if row - (col - c) >= 0 and self.board[row - (col - c)][c] == 1:
                return False
            if row + (col - c) < self.n and self.board[row + (col - c)][c] == 1:
                return False
        return True

    def print_solution(self):
        self.solution = []
        for row in range(self.n):
            queen_col = None
            for col in range(self.n):
                if self.board[row][col] == 1:
                    queen_col = col
                    break
            self.solution.append(queen_col)

        print("Solution:")
        for row in range(self.n):
            line = ""
            for col in range(self.n):
                if self.solution[row] == col:
                    line += "Q "
                else:
                    line += ". "
            print(line)


# Example usage:
n = int(input("Enter the number of queens: "))  # Number of queens and board size
queens = NQueens(n)
queens.solve()
