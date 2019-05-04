
board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
def makeboard(board):
    """
    This defenition prints the board throught out all the changes made by the players.
    """
    print (board[1], '|', board[2], '|', board[3])
    print('----------')
    print (board[4], '|', board[5], '|', board[6])
    print('----------')
    print (board[7], '|', board[8], '|', board[9])





def check_if_space_free(board, position):
    """
    This is to see if that position is taken from the player input for their move
    """
    if board[position] == " ":
        return True
    else:
        return False


def player_input_move(board, player):
    """
    This will take input from the player.
    check if that position is available,
    if it is not available player will be asked for another input.
    if available, players key will be placed on board.
    """
    choice = ''
    while((choice not in '1 2 3 4 5 6 7 8 9'.split() or not check_if_space_free(board, int(move)))):
        choice = input("{a}  what position do you want to choose from 1-9?".format(a=player))
    return int(choice)


def check_board_full(board, check_if_space_free):
    """
    This will check if there are any available places in the Tic Tac Toe board.
    """
    for num in board(range(1,10)):
        if check_if_space_free(board, num):
            return False
        else:
            return True


while True:
    '''main function for game.runs untill a the loop is  exited using break'''
    os.system('clear')
    print('        \t                   Welcome To                           ')
    print('          \t                TIC     TAC     TOE                           \n')
    time.sleep(.4)
    board = [' '] * 10
    print('\t\t\t\t   _1|_2_|_3__')
    print('\t\t\t\t   _4|_5_|_6_')
    print('\t\t\t\t    7| 8 | 9 \n')
    name = piecesForPlayers()
    turn = whosFirst()
    print("{a} will go first".format(a=name[turn]))
    time.sleep(.3)
    game_on = True
    time.sleep(1)
    while game_on:
        if turn == "X":
            # player 1
            makeboard(board)
            status_fullboard = check_board_full(board, check_if_space_free)
            if winCheck(board, "O"):
                print("Congrats {a} is the winner".format(a=name["O"]))
                break
            if status_fullboard:
                print("oops!its a tie")
                break
            position = player_input_move(board, name["X"])
            status_position = check_if_space_free(board, position)
            if status_position == True:
                position_board(position, board, "X")

            turn = "O"


        else:
            # player2
            makeboard(board)
            status_fullboard = check_board_full(board, check_if_space_free)
            if winCheck(board, "X"):
                print("congrats {a} is the winner".format(a=name["X"]))
                break
            if status_fullboard:
                print("oops!its a tie")
                break
            position = player_input_move(board, name["O"])
            status_position = check_if_space_free(board, position)
            if status_position == True:
                position_board(position, board, "O")

            turn = "X"
    if replay():
        continue
    else:
        print("Thank You for playing Tic Tac Toe BY Noobie Noobie\n bye bye bye")
        time.sleep(.7)
        os.system('clear')
        break