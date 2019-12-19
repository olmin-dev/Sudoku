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

# Return True if the proposition is correct (according the sudoku's rules)
def isCorrect(a, test, x, y):
    for i in range(len(a)):
        if(a[x][y] != 0 or a[i][x] == test or a[y][i] == test):
            return False
    return True

# Add a nulber in the board only if it's possible
def addNumber(a, val, x, y):
    if(isCorrect(a, val, x, y)):
        a[x][y] = val
        return True
    return False

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
