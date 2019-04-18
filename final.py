playerOne = input("player one, what is your name?" )
playerTwo = input("player two, what is your name?" )

def whosFirst():
    import random
    n = random.randint(1, 2)
    if n == 1:
        print(playerOne, "you are first.")
        return playerOne
    else:
        print(playerTwo, "you are first.")
        return playerTwo

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

whosFirst()
