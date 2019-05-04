
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


