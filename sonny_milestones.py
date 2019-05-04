playerOne = input("player one, what is your name?" )
playerTwo = input("player two, what is your name?" )
import random

def whosFirst(p1, p2):
    """decides whos first. 50/50 chance."""
    n = random.randint(1, 2)
    if n == 1:
        print(p1, "you are first.")
        return p1
    else:
        print(p2, "you are first.")
        return p2

def piecesForPlayers(p1name, p2name):
    """assigns x or o to first players choice. allows players to input again if x or o not entered."""
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

def board_position(posi, board, plyr):
    """
    places  player input to a position in list. list is board
    """
    board[posi] = player

def winCheck(board, plyr):
    """
    looks at possible win combos to check for winner
    """
    return (board[0] == board[1] == board[2] == plyr or
           board[3] == board[4] == board[5] == plyr or
           board[6] == board[7] == board[8] == plyr or
           board[0] == board[3] == board[6] == plyr or
           board[1] == board[4] == board[7] == plyr or
           board[2] == board[5] == board[8] == plyr or
           board[0] == board[4] == board[8] == plyr or
           board[6] == board[4] == board[2] == plyr)

def replay():
    """
    boolean. asks users to replay? for 'yes' input returns true otherwise returns false
    """
    decision = input("do you want to play again?").lower()
    if decision == 'yes':
        return True

pieces = piecesForPlayers(playerOne, playerTwo)


print("Player 1 name is", playerOne, "and their piece is", pieces[0])
print("Player 2 name is", playerTwo, "and their piece is", pieces[1])

firstPlayer = whosFirst(playerOne, playerTwo)
print(firstPlayer)


