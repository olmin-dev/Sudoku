# Sudoku

## I) Sudoku solver

The first goal of this project is to create a sudoku solver that can solve any solvable sudoku given.
I will use backtracking technology to implement the solver

## II) Sudoku game with a simple GUI

Then I would like to learn a specific GUI in which players can send proposition.
I think the first step will be to print the sudoku board with the GUI.
Then add the possibility to send proposition these will be controled by the solver.
I would like to implement a score system with a leaderboard :
  - Every day a random board is created (thx to a sid calculated with the date)
  - Every player can choose the difficulty (that is to say the number of empty case. For each difficulty it's exactly the same board which is created)
  - When someone succed the sudoku, a score based on the time he took to solve the game, the difficulty and the errors' number.
  - Then this scrore will be add to an online database which is linked with a website showing the leaderboard

## III) AI

The last thing I would like to implement is a set of AI solver that are based on different technology and knowledges:
  - A understanding AI that is to say an AI following basic I use to solve Sudoku
  - A multi thread solver (same as before but with some threads)
  - A pattern matching solver (same as the first AI but with some rules of pattern maching. The hard part will be to find the right pattern. Maybe a kind of machine learning recognition pattern Ai can be use)
  - A machine learning solver (I don't know yet how i will do this but it's a challenging goal)

## IV) Bonus

Here, I will seak about all the possible adds that can be interesting with this project but will for sure note be iplemented:
  - New rules of sudoku (for example case of  number, more column/line number and possibility to have so double number, ...tec)
  - A three-dimensionnal sudoku game (there is no more a simple sudoku but 9 Sudokus linked one with each other like in a cube. It will be somehow realy challenging to find a correct board so a solver will be hard enough)
  - A colored sudoku (each case contains between 1 and 3 numbers. Each red case have to solve the red part's sudoku that is to say the sudoku formed by all the numbers with a not null red part (Example: a yellow number take part ot the red and green sudoku). Finding a solution can be difficult but I think that the colored sudoku soolver will be quiet easy to implement)
