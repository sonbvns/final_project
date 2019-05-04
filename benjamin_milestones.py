
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
