
while True:
    '''main function for game. Will run until users decide'''

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

