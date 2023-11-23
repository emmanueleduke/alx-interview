# 8 Queen problem
# Simple loop solution

numQueens = 8  # Number of queens solving for
currentSolution = [0 for x in range(numQueens)]  # Will hold current testing data
solutions = []  # Found solutions

def isSafe(testRow, testCol):
    # No need to check for row 0
    if testRow == 0:
        return True

    for row in range(0, testRow):
        # Check vertical
        if testCol == currentSolution[row]:
            return False

        # Diagonal
        if abs(testRow - row) == abs(testCol - currentSolution[row]):
            return False

    # No attack found
    return True

for queen0 in range(numQueens):
    if not isSafe(0, queen0):
        continue
    else:
        currentSolution[0] = queen0

    for queen1 in range(numQueens):
        if not isSafe(1, queen1):
            continue
        else:
            currentSolution[1] = queen1

        for queen2 in range(numQueens):
            if not isSafe(2, queen2):
                continue
            else:
                currentSolution[2] = queen2

            for queen3 in range(numQueens):
                if not isSafe(3, queen3):
                    continue
                else:
                    currentSolution[3] = queen3

                for queen4 in range(numQueens):
                    if not isSafe(4, queen4):
                        continue
                    else:
                        currentSolution[4] = queen4

                    for queen5 in range(numQueens):
                        if not isSafe(5, queen5):
                            continue
                        else:
                            currentSolution[5] = queen5

                        for queen6 in range(numQueens):
                            if not isSafe(6, queen6):
                                continue
                            else:
                                currentSolution[6] = queen6

                            for queen7 in range(numQueens):
                                if not isSafe(7, queen7):
                                    continue
                                else:
                                    currentSolution[7] = queen7
                                    solutions.append(currentSolution.copy())

print(len(solutions), "solutions found")
for solution in solutions:
    print(solution)

