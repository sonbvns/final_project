
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

