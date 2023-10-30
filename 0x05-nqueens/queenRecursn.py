# N Queen problem
# Recursive solution

numQueens = 8 # num of queens to solve for

currentSolution = [0 for x in range(numQueens)] # will hold current testing data
solutions = [] # found solution

def isSafe(testRow, testCol):
    # no need checking for row 0
    if testRow == 0:
        return True

    for row in range(0, testRow):
        # check vertical
        if testCol == currentSolution[row]:
            return False

        # diagonal
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    # no attack found
    return True

def placeQueen(row):
    global currentSolution, solutions, numQueens

    for col in range(numQueens):
        if not isSafe(row, col):
            continue
        else:
            currentSolution[row] = col
            if row == (numQueens - 1):
                # last row
                solutions.append(currentSolution.copy())
            else:
                placeQueen(row + 1)

placeQueen(0)

print(len(solutions), "solutions found")
for solution in solutions:
    print(solution)
