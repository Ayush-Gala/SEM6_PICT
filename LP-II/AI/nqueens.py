#BRANCH AND BOUND SOLUTION

class NQueens:
    def __init__(self, n):
        self.n = n
        self.columns = []
        self.diag1 = []        #diagonal  /
        self.diag2 = []        #diagonal \
        self.solutions = []     # list to store all the solutions
    
    # def draw(self, solution):
    #     for elem in solution:
    #         for j in range(n):
    #             if j == elem:
    #                 print("|Q ",end="")
    #             else:
    #                 print("|  ", end="")
    #         print("|")
    #         for j in range(n):
    #             print("---", end="")
    #             print("")
    #     print("\n\n\n")

    def solve(self):
        self.search(0, [])
        return self.solutions
 
    #branch and bound code
    def search(self, row, solution):
        if row == self.n:
            self.solutions.append(solution)
        else:
            for col in range(self.n):
                if col not in self.columns and row - col not in self.diag1 and row + col not in self.diag2:
                    self.columns.append(col)
                    self.diag1.append(row - col)
                    self.diag2.append(row + col)
                    # self.draw(solution)                 
                    self.search(row + 1, solution + [col])  #recursive call to search function
                    self.columns.pop()
                    self.diag1.pop()
                    self.diag2.pop()


#BACKTRACKING SOLUTION

class NQueensSolver:
    def __init__(self, n):
        self.n = n
        self.board = [['.' for _ in range(n)] for _ in range(n)]
        self.solutions = []
    
    def solve(self):
        self.backtrack(0)
        return self.solutions
    
    def backtrack(self, row):
        if row == self.n:
            self.solutions.append([''.join(row) for row in self.board])
            return
        for col in range(self.n):
            if self.is_safe(row, col):
                self.board[row][col] = 'Q'
                self.backtrack(row + 1)
                self.board[row][col] = '.'
    
    def is_safe(self, row, col):
        for i in range(self.n):
            if self.board[row][i] == 'Q':
                return False
        for i in range(self.n):
            if self.board[i][col] == 'Q':
                return False
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i, j = i - 1, j - 1
        i, j = row, col
        while i < self.n and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i, j = i + 1, j + 1
        i, j = row, col
        while i >= 0 and j < self.n:
            if self.board[i][j] == 'Q':
                return False
            i, j = i - 1, j + 1
        i, j = row, col
        while i < self.n and j >= 0:
            if self.board[i][j] == 'Q':
                return False
            i, j = i + 1, j - 1
        return True


# Take input from the user
n = int(input("Enter the number of queens to consider: "))
 
# Solve the n-queens problem
method = int(input("Which technique do you want to use?\n1. Branch and Bound\n2. Backtracking\nEnter your choice: "))
if method == 1:
    solver = NQueens(n)
else:
    solver = NQueensSolver(n)
solutions = solver.solve()
 
# Print the solutions
print("Number of solutions:", len(solutions))
print(solutions)
i=0
for solution in solutions:
    i+=1
    print("\n\nSolution: ", i,":\n\n")
    for elem in solution:
        for j in range(n):
            if j == elem:
                print("|Q ",end="")
            else:
                print("|  ", end="")
        print("|")
        for j in range(n):
            print("---", end="")
        print("")
    # print(solution)



