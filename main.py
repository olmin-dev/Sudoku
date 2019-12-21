# Creates an empty sudoku board
def createEmptyGame():
    ret = []
    for i in range(9):
        ret.append([])
        for j in range(9):
            ret[i].append(0) # 0 means empty
    return ret

# Prints the sudoku board
# board is the Sudoku board that we want to print
def printSudoku(board): # TODO Update with the GUI
    for i in range(9):
        print(str(board[i][0:3])[1:-1].replace(", ", " ").replace("0", "X"), "|",
            str(board[i][3:6])[1:-1].replace(", ", " ").replace("0", "X"), "|",
            str(board[i][6:9])[1:-1].replace(", ", " ").replace("0", "X"))
        if(i % 3 == 2 and i < 8):
            print("------+-------+-------")


# Tests if the number already exist in the square
# @Param board is the Sudoku board in which we want to make our test
# @Param val is the value we want to test
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def isAlreadyInSquare(board, val, x, y):
    xmin = (x // 3) * 3
    ymin = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if(not(x == xmin + i and y == ymin + j) and board[xmin + i][ymin + j] == val):
                return True
    return False

# Tests if the number already exist in the line
# @Param board is the Sudoku board in which we want to make our test
# @Param val is the value we want to test
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def isAlreadyInLine(board, val, x, y):
    for i in range(9):
        if(y != i and board[x][i] == val):
            return True
    return False

# Tests if the number already exist in the column
# @Param board is the Sudoku board in which we want to make our test
# @Param val is the value we want to test
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def isAlreadyInColumn(board, val, x, y):
    for i in range(9):
        if(x != i and board[i][y] == val):
            return True
    return False

# Tests if the number already exist in the square
# @Param board is the Sudoku board in which we want to make our test
# @Param val is the value we want to test
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def isAlreadyIn(board, val, x, y):
    return isAlreadyInSquare(board, val, x, y) or isAlreadyInLine(board, val, x, y) or isAlreadyInColumn(board, val, x, y)

# Tests if the proposition is correct (according the sudoku's rules)
# @Param board is the Sudoku board in which we want to make our test
# @Param val is the value we want to test
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def isCorrect(board, val, x, y):
    return not(isAlreadyIn(board, val, x, y))

# Add a nulber in the board only if it's possible
# @Param board is the Sudoku board in which we want to add a proposition
# @Param val is the value we want to add
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def addNumber(board, val, x, y):
    if(isCorrect(board, val, x, y)):
        board[x][y] = val
        return True
    return False

# Verfiy if the Sudoku board is is is correct
# board is the Sudoku board we want to verify
def isCorrectBoard(board):
    for i in range(9):
        for j in range(9):
            if(board[i][j] != 0 and isAlreadyIn(board, board[i][j], i, j)):
                return False
    return True

# Return all the position that have to be solved
# board is the Sudoku board in which we want to know the empty positions
def toSolve(board):
    ret = []
    for  i in range(9):
        for j in range(9):
            if(board[i][j] == 0):
                ret.append((i, j, 0))
    return ret

# Delete the proposition at position (i, j)
# @Param board is the Sudoku board in which we want to delete the proposition
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
def deleteNumber(board, x, y):
    board[x][y] = 0

# Goes thorugh the process of backtracking
# @Param board is the Sudoku board we want to solve
# @Param val is the proposition's value
# @Param x is the proposition's ordinate value
# @Param y is the proposition's abscissa value
# @Param toSolveStack is the stack which contains all the positions to solve
# @Param solvedStack is the stack which contains all the positions already solved
def backtracking(board, val, x, y, toSolveStack, solvedStack):
    if(val == 9): #Backtracking step
        if(solvedStack == []):
            raise Exception("There is no solution")
        toSolveStack.append((x, y, 0))
        (x, y, k) = solvedStack.pop()
        deleteNumber(board, x, y)
        toSolveStack.append((x, y, k))
        return False
    return True

# Backtracking solver
# @Param board is the Sudoku board we want to solve
def backtrackingSolver(board):
    if(not(isCorrectBoard(board))):
        raise Exception("The Sudoku board is not correct")
    toSolveStack = toSolve(board)
    solvedStack = []
    while toSolveStack != []:
        (i, j, k) = toSolveStack.pop()
        if(backtracking(board, k, i, j, toSolveStack, solvedStack)):
            bt = True
            k += 1
            while(bt):
                if(isCorrect(board, k, i, j)):
                    solvedStack.append((i, j, k))
                    addNumber(board, k, i, j)
                    bt = False
                else:
                    if(not(backtracking(board, k, i, j, toSolveStack, solvedStack))):
                        bt = True
                k += 1

# General solver
# @Param board is the Sudoku board we want to solve
# @Param type is the type of solver that will be use
def solver(board, type):
    print("Sudoku to solve:")
    printSudoku(board)
    if(type == "bt"):
        backtrackingSolver(board)
    print("Solution:")
    printSudoku(board)

# Board example
test = [[0,0,0,0,5,7,0,4,0],
        [2,0,4,6,0,8,0,0,9],
        [5,8,9,2,0,4,0,7,1],
        [0,0,7,3,6,5,1,0,0],
        [6,0,2,1,0,9,4,0,7],
        [0,0,3,7,4,2,8,0,0],
        [9,3,0,8,0,1,5,2,4],
        [0,0,8,5,0,3,7,0,6],
        [0,1,0,4,2,0,0,0,0]]

# Solution:
# 3 6 1 | 9 5 7 | 2 4 8
# 2 7 4 | 6 1 8 | 3 5 9
# 5 8 9 | 2 3 4 | 6 7 1
# ------+-------+-------
# 8 4 7 | 3 6 5 | 1 9 2
# 6 5 2 | 1 8 9 | 4 3 7
# 1 9 3 | 7 4 2 | 8 6 5
# ------+-------+-------
# 9 3 6 | 8 7 1 | 5 2 4
# 4 2 8 | 5 9 3 | 7 1 6
# 7 1 5 | 4 2 6 | 9 8 3
