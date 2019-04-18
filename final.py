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


pieces = piecesForPlayers(playerOne, playerTwo)

print("Player 1 name is", playerOne, "and their piece is", pieces[0])
print("Player 2 name is", playerTwo, "and their piece is", pieces[1])

firstPlayer = whosFirst(playerOne, playerTwo)
print(firstPlayer)


