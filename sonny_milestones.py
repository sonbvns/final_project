playerOne = input("player one, what is your name?" )
playerTwo = input("player two, what is your name?" )
import random

def whosFirst(p1, p2):
    n = random.randint(1, 2)
    if n == 1:
        print(p1, "you are first.")
        return p1
    else:
        print(p2, "you are first.")
        return p2

def piecesForPlayers(p1name, p2name):
    done = True
    while done is True:
        char = input(p1name + " would you like to be X or O?: ")
        if char == "X":
            plyr1 = "X"
            plyr2 = "O"
            done = False
        elif char == "O":
            plyr1 = "O"
            plyr2 = "X"
            done = False
        else:
            print("you either did not type “X” or ”O” or you entered something else entirely, try again.")
    print(p2name , "You are ", plyr2)
    return (plyr1, plyr2)

def board_position(position,board,player):
	"""
	places  player input to a position in list. list is board
	"""
	board[position] = player

def winCheck(board,player):
    """
    looks at possible win combos to check for winner
    """
  return (board[0] == board[1] == board[2] == player or
           board[3] == board[4] == board[5] == player or
           board[6] == board[7] == board[8] == player or
           board[0] == board[3] == board[6] == player or
           board[1] == board[4] == board[7] == player or
           board[2] == board[5] == board[8] == player or
           board[0] == board[4] == board[8] == player or
           board[6] == board[4] == board[2] == player)

def replay():
	"""
	boolean function:asks users for replay.for Y.... input returns True otherwise returns false
	"""
	decision = input("Do you want to play again????").lower()
	if decision == 'yes':
		return True

pieces = piecesForPlayers(playerOne, playerTwo)


print("Player 1 name is", playerOne, "and their piece is", pieces[0])
print("Player 2 name is", playerTwo, "and their piece is", pieces[1])

firstPlayer = whosFirst(playerOne, playerTwo)
print(firstPlayer)


