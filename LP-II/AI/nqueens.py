class NQueens:
    def __init__(self, n):
        self.n = n
        self.columns = []
        self.diag1 = []        #diagonal  /
        self.diag2 = []        #diagonal \
        self.solutions = []     # list to store all the solutions
 
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
                    self.search(row + 1, solution + [col])  #recursive call to search function
                    self.columns.pop()
                    self.diag1.pop()
                    self.diag2.pop()
 
# Take input from the user
n = int(input("Enter the number of queens to consider: "))
 
# Solve the n-queens problem
solver = NQueens(n)
solutions = solver.solve()
 
# Print the solutions
print("Number of solutions:", len(solutions))
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
