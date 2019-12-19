# Create an empty sudoku board
def createEmptyGame():
    ret = []
    for i in range(9):
        ret.append([])
        for j in range(3):
            ret[i].append([])
            for k in range(3):
                ret[i][j].append(0) # 0 means empty
    return ret

# Print the sudoku board
def printSudoku(a): #TODO implement a better print structure
    for i in range(9):
        print("------------")
        printSudokuCase(a[i])

# Print one 9x9 case (Will be deleted)
def printSudokuCase(a):
    for i in range(3):
        print(a[i])

# Return True if the number already exist in the square
def isAlreadyInSquare(a, test):
    for i in range(3):
        for j in range(3):
            if(a[i][j] == test):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyInColumn(a, test, x, y, n):
    for i in range(3):
        for j in range(3):
            if(a[i*3 + n][x][j] == test):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyInLine(a, test, x, y, n):
    for i in range(3):
        for j in range(3):
            if(a[(n // 3) + i][j][y] == test):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyIn(a, test, x, y, n):
    return not(isAlreadyInSquare(a[n], test)) and not(isAlreadyInLine(a, test, x, y, n)) and not(isAlreadyInColumn(a, test, x, y, n))

# Return True if the proposition is correct (according the sudoku's rules)
def isCorrect(a, test, n, x, y):
    for i in range(len(a)):
        if(not(isAlreadyIn(a[i], test, x, y, n))):
            return False
    return True

# Add a nulber in the board only if it's possible
def addNumber(a, val, x, y):
    if(isCorrect(a, val, x, y)):
        a[x][y] = val
        return True
    return False

# Return all the position that have to be solved
def toSolve(a):
    ret = []
    for  i in range(9):
        for j in range(3):
            for k in range(3):
                if(a[i][j][k] == 0):
                    ret.append((i, j, k))
    return ret

# First verion of the solver
def backtrackingSolver(a):
    toSolve = toSolve(a)
    for (i, j, k) in toSolve:
        for l in range(9):
            if(isCorrect(a, l, i, j, k)):
                addNumber(a, l, i, j, k)

# Board example TODO : Search a real sudoku board
test = [[[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]],
        [[1,2,3],[4,5,6],[7,8,0]]]

printSudoku(test)

print(toSolve(test))

print(isAlreadyIn(test, 5, 0, 1, 2))
