#Playerone = input('Player one, what is your name?')
#Playertwo = input('Player two, what is your name?')


board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
def makeboard():
    board = ['0', '1', '2', '3', '4', '5', '6', '7', '8']
    print (board[0], '|', board[1], '|', board[2])
    print('----------')
    print (board[3], '|', board[4], '|', board[5])
    print('----------')
    print (board[6], '|', board[7], '|', board[8])

makeboard()




def pieceForPlayer(p1name, p2name):
    done = True
    while done is True:
        char = input(p1name + ", would you like to be X or O?:")
        if char == "X":
            plyr1 = "X"
            plyr2 = "O"
            print(p1name + ", you are X. " + p2name + ", you are O.")
            done = False
        else:
            plyr1 = "O"
            plyr2 = "X"
            print(p1name + ", you are O. " + p2name + ", you are X.")
            done = False
    print()
    return (plyr1, plyr2)




def whosFirst():
    import random
    random.randint(1, 2)
    if random.randint == 1:
        return playerOne
    else:
        return playerTwo




def check_if_space_free(board, position):
  """
  This is to see if that position is taken from the player input for their move
  """
  if board[position] == '':
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
  move = ''
  while((choice not in '1 2 3 4 5 6 7 8 9'.split() or not check_if_space_free(board, int(move)))):
    print(Format to the right player ", what is your next move? (1-9)")
    move = input()
  return int(move)

def check_board_full(board, check_if_space_free):
    """

    :param board:
    :param check_if_space_free:
    :return:
    """
    for num in board(range(1,10)):
        if check_if_space_free(board, num):
            return False
    else:
        return True


#main Program

#pieceForPlayer(Playerone, Playertwo)
