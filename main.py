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
            if(not(x == xmin + i and y != ymin + j) and board[xmin + i][ymin + j] == val):
                return True
    return False

# Return True if the number already exist in the square
def isAlreadyInLine(board, val, x, y):
    for i in range(9):
        print(board[x][i], x, i, y, val)
        if(y != i and board[x][i] == val):
            return True
    return False

# Return True if the number already exist in the square
def isAlreadyInColumn(board, val, x, y):
    for i in range(9):
        if(x != i and board[i][y] == val):
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

# Verfiy if the Sudoku board is is is correct
def isCorrectBoard(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] != 0 and isAlreadyIn(board, board[i][j], i, j)):
                return False
    return True

# Return all the position that have to be solved
def toSolve(board):
    ret = []
    for  i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                ret.append((i, j))
    return ret

# Backtracking function
def backtrack(board, solvedStack, toSolveStack):
    if(solvedStack == []):
        return False
    (i, j) = solvedStack.pop()
    init_val = board[i][j]
    for val in range(init_val + 1, 10):
        if(isCorrect(board, val, i, j)):
            solvedStack.append((i, j))
            addNumber(board, val, i, j)
            return False
        else :
            if(val == 9):
                toSolveStack.append((i, j))
                backtrack(board, solvedStack, toSolveStack)

# First verion of the solver
def backtrackingSolver(board):
    if(isCorrectBoard(board)):
        return False
    toSolveStack = toSolve(board)
    solvedStack = []
    while toSolveStack != []:
        print("--------------------------")
        (i, j) = toSolveStack.pop()
        for val in range(1, 10):
            if(isCorrect(board, val, i, j)):
                solvedStack.append((i, j))
                addNumber(board, val, i, j)
                print(i, j, val)
                printSudoku(board)
                break
            # else:
            #     print("ca part", i, j)
            #     if(val == 9):
            #         print("Backtrack")
            #         toSolveStack.append((i, j))
            #         backtrack(board, solvedStack, toSolveStack)

# Board example TODO : Search a real sudoku board
test = [[0,0,0,0,5,7,0,4,0],
        [2,0,4,6,0,8,9,0,0],
        [5,8,9,2,0,4,0,7,1],
        [0,0,7,3,6,5,1,0,0],
        [6,0,2,1,0,9,4,0,7],
        [0,0,3,7,4,2,8,0,0],
        [9,3,0,8,0,1,5,2,4],
        [0,0,8,5,0,3,7,0,6],
        [0,1,0,4,2,0,0,0,0]]

# printSudoku(test)
print(toSolve(test))
backtrackingSolver(test)
# printSudoku(test)
