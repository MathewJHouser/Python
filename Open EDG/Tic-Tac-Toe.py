from random import randrange

def display_board(board):
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print("|   " + str(row[0]) + "   |   " + str(row[1]) + "   |   " + str(row[2]) + "   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

def enter_move(board):
    try:
        move = int(input("Enter your move: "))
    except:
        print("Please enter a number between 1 and 9.")
        enter_move(board)
    spaces = []
    for i in range(3):
        for j in range(3):
            if (i, j) in free:
                spaces.append(board[i][j])
    if move not in spaces:
        print("This Space is already taken. Please enter a number between 1 and 9.")
        enter_move(board)
    else:
        for i in range(3):
            for j in range(3):
                if (board[i][j]) == move:
                    if (i, j) in free:
                        board[i][j] = "O"
                    else:
                        print("This space is already taken.")
                        enter_move(board)
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.


def make_list_of_free_fields(board):
    global free
    free = []
    for i in range(3):
        for j in range(3):
            if str(board[i][j]) not in "XO":
                free.append((i, j))
    # The function browses the board and builds a list of all the free squares;
    # the list consists of tuples, while each tuple is a pair of row and column numbers.

def victory_for(board, sign):
   global yes
   for i in range(3):
        for j in range(3):
            if board[i][0] == board[i][1] == board[i][2] == sign or \
                    board[0][j] == board[1][j] == board[2][j] == sign or \
                    board[0][0] == board[1][1] == board[2][2] == sign or \
                    board[2][0] == board[1][1] == board[0][2] == sign:
                if sign == "X":
                    print("I won!")
                    yes = False
                    break
                elif sign == "O":
                    print("You won!")
                    yes = False
                    break
                elif len(free) == 0:
                    print("We Tied!")
                    yes = False
                    break

    # The function analyzes the board's status in order to check if
    # the player using 'O's or 'X's has won the game


def draw_move(board):
    spaces = []
    for i in range(3):
        for j in range(3):
            if (i, j) in free:
                spaces.append(board[i][j])
    index = randrange(len(free))
    move = spaces[index]
    for i in range(3):
        for j in range(3):
            if board[i][j] == move:
                board[i][j] = "X"
    #The function draws the computer's move and updates the board.



global board
board = [[1,2,3], [4,"X",6], [7,8,9]]
global yes
yes = True
print("Let's play Tic-Tac-Toe, I'll go first. ")
display_board(board)
turn = 1
while yes:
    if turn % 2:
        print("Your Turn!")
        make_list_of_free_fields(board)
        enter_move(board)
        display_board(board)
        victory_for(board, "O")
    if turn % 2 == 0:
        print("My Turn!")
        make_list_of_free_fields(board)
        draw_move(board)
        display_board(board)
        victory_for(board, "X")
    turn+=1