# The sudoku's board structure is just a 9-element-list which contains 9-element-list containing integer between 0 and 9

# Create an empty sudoku board
def createEmptyGame():
    ret = []
    for i in range(9):
        ret.append([])
        for j in range(9):
            ret[i].append(0) # 0 means empty
    return ret

# Print the sudoku board
def printSudoku(a): # Update with the GUI
    for i in range(9):
        print(str(a[i][0:3])[1:-1].replace(", ", " ").replace("0", "X"), "|",
            str(a[i][3:6])[1:-1].replace(", ", " ").replace("0", "X"), "|",
            str(a[i][6:9])[1:-1].replace(", ", " ").replace("0", "X"))
        if(i % 3 == 2 and i < 8):
            print("------+-------+-------")


# Return True if the number already exist in the square
def isAlreadyInSquare(board, val, x, y):
    xmin = (x // 3) * 3
    ymin = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if(board[xmin + i][ymin + j] == val):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyInColumn(board, val, x, y):
    for i in range(9):
            if(board[x][i] == val):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyInLine(board, val, x, y):
    for i in range(9):
            if(board[i][y] == val):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyIn(board, val, x, y):
    return isAlreadyInSquare(board, val, x, y) or isAlreadyInLine(board, val, x, y) or isAlreadyInColumn(board, val, x, y)

# Return True if the proposition is correct (according the sudoku's rules)
def isCorrect(board, val, x, y):
    return board[x][y] == 0 and not(isAlreadyIn(board, val, x, y))

# Add a nulber in the board only if it's possible
def addNumber(board, val, x, y):
    if(isCorrect(board, val, x, y)):
        board[x][y] = val
        return True
    return False

# Return all the position that have to be solved
def toSolve(board):
    ret = []
    for  i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                ret.append((i, j))
    return ret

# First verion of the solver
def backtrackingSolver(board):
    empty = toSolve(board)
    for (i, j) in empty:
        for val in range(1, 10):
            print(val, i, j)
            if(isCorrect(board, val, i, j)):
                addNumber(board, val, i, j)

# Board example TODO : Search a real sudoku board
test = [[1,2,3,4,5,6,7,8,0],
        [0,1,2,3,4,5,6,7,8],
        [1,0,2,3,4,5,6,7,8],
        [1,2,0,3,4,5,6,7,8],
        [1,2,3,0,4,5,6,7,8],
        [1,2,3,4,0,5,6,7,8],
        [1,2,3,4,5,0,6,7,8],
        [1,2,3,4,5,6,0,7,8],
        [1,2,3,4,5,6,7,0,8]]

printSudoku(test)
print(addNumber(test, 9, 8, 8))
printSudoku(test)
print(toSolve(test))
backtrackingSolver(test)
printSudoku(test)
