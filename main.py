




def makeboard(board):
    """
    This defenition prints the board throught out all the changes made by the players.
    """

    print (board[1], '|', board[2], '|', board[3])
    print('----------')
    print (board[4], '|', board[5], '|', board[6])
    print('----------')
    print (board[7], '|', board[8], '|', board[9])








def player_input_move(board, plyr):
    """
    This will take input from the player.
    check if that position is available,
    if it is not available player will be asked for another input.
    if available, players key will be placed on board.
    """
    choice = ''
    while((choice not in '1 2 3 4 5 6 7 8 9'.split() or not check_if_space_free(board, int(choice)))):
        choice = input("\n {a} what position do you want to choose from 1-9?\n".format(a=plyr))
    return int(choice)

def check_if_space_free(board, posi):
    """
    This is to see if that position is taken from the player input for their move
    """
    if board[posi] == " ":
        return True
    else:
        return False

def check_board_full(board, freespace):
    """
    This will check if there are any available places in the Tic Tac Toe board.
    """
    for num in range(1, 10):
        if freespace(board, num):
            return False
    else:
        return True



def whosFirst(p1, p2):
    """decides whos first. 50/50 chance."""
    n = random.randint(1, 2)
    if n == 1:
        print(p1, ", you are first.\n \n")
        return p1
    else:
        print(p2, ", you are first.\n \n ")
        return p2

def piecesForPlayers(p1name, p2name):
    """assigns x or o to first players choice. allows players to input again if x or o not entered."""
    done = True
    while done is True:
        char = input(p1name + " would you like to be X or O?: \n")
        if char == "X":
            plyr1 = "X"
            plyr2 = "O"
            name = {"X" : plyr1, "O" : plyr2}
            done = False
        elif char == "O":
            plyr1 = "O"
            plyr2 = "X"
            name = {"O": plyr1, "X": plyr2}
            done = False
        else:
            print("you either did not type “X” or ”O” or you entered something else entirely, try again.")
    print(p2name , "you are, ", plyr2, "\n")
    return (name)

def board_position(posi, board, plyr):
    """
    places  player input to a position in list. list is board
    """
    board[posi] = plyr

def winCheck(board, plyr):
    """
    looks at possible win combos to check for winner
    """
    return (board[1] == board[2] == board[3] == plyr or
            board[4] == board[5] == board[6] == plyr or
            board[7] == board[8] == board[9] == plyr or
            board[1] == board[4] == board[7] == plyr or
            board[2] == board[5] == board[8] == plyr or
            board[3] == board[6] == board[9] == plyr or
            board[1] == board[5] == board[9] == plyr or
            board[7] == board[5] == board[3] == plyr)

def replay():
    """
    boolean. asks users to replay? for 'yes' input returns true otherwise returns false
    """
    decision = input("\ndo you want to play again?\n").lower()
    if decision == 'yes':
        return True




while True:
    '''main function for game.runs untill a the loop is  exited using break'''

    print('\nWelcome to Sonny and Benjamins Python Tic Tac Toe game')
    print('\nWe hope you enjoy the fun game we have created!\n')
    board = [' '] * 10
    print(1, '|', 2, '|', 3)
    print('----------')
    print(4, '|', 5, '|', 6)
    print('----------')
    print(7, '|', 8, '|', 9)

    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    playerOne = input("\nplayer one, what is your name?")
    playerTwo = input("\nplayer two, what is your name?\n")
    name = piecesForPlayers(playerOne, playerTwo)
    import random
    turn = whosFirst(playerOne, playerTwo)
    game_on = True
    while game_on:
        if turn == "X":
            # player 1
            makeboard(board)
            status_fullboard = check_board_full(board, check_if_space_free)
            if winCheck(board, "O"):
                print("\nCongrats {a} is the winner".format(a=name["O"]))
                break
            if status_fullboard:
                print("\noops! It is a tie :o")
                break
            position = player_input_move(board, name["X"])
            status_position = check_if_space_free(board, position)
            if status_position == True:
                board_position(position, board, "X")

            turn = "O"


        else:
            # player2
            makeboard(board)
            status_fullboard = check_board_full(board, check_if_space_free)
            if winCheck(board, "X"):
                print("\nCongrats {a} is the winner".format(a=name["X"]))
                break
            if status_fullboard:
                print("\nOops! It is a tie :/")
                break
            position = player_input_move(board, name["O"])
            status_position = check_if_space_free(board, position)
            if status_position == True:
                board_position(position, board, "O")

            turn = "X"
    if replay():
        continue
    else:
        print("\nWOAH DUDE!\nThank You for playing Tic Tac Toe\nHave a good summer!")
        break

