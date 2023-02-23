


# board
def draw_board(spots):
    board = (f'{spots[1]} | {spots[2]} | {spots[3]}\n'
             f'{spots[4]} | {spots[5]} | {spots[6]}\n'
             f'{spots[7]} | {spots[8]} | {spots[9]}\n')

    print(board)


# score
def show_score(player_1, player_2, score):
    score_player_1, score_player_2 = score[player_1], score[player_2]

    player_score = (
        f'{player_1} {score_player_1} || {score_player_2} {player_2}')

    print(player_score)


# register two players
def register_player(players):
    num_players = 1
    while num_players < 3:
        print(f'Player {num_players} must choose a username.')
        set_username(players)
        num_players += 1

# sets each player's username
def set_username(players):
    while True:
        username = input('Username: ')
        if len(username) < 5 or len(username) > 12 or not username.isalpha():
            print(
                "The username must have between 5 and 12 characters, without numbers or symbols.")
        else:
            players[username] = None
            break

# sets the a mark for each player
def set_player_mark(player_1, player_2, player, mark_1, mark_2, players, score):
    default_score = 0
    while True:
        mark = int(
            input(f'{player}, choose between 1 for "{mark_1}" or 2 for "{mark_2}": '))
        if mark == 1 or mark == 2:
            if mark == 1:
                players.update({player_1: mark_1, player_2: mark_2})
                print(
                    f'\n{player_1} chose "{mark_1}". {player_2} got "{mark_2}".\n')
                score.update({player_1: default_score,
                             player_2: default_score})
                break

        elif mark == 2:
            players.update({player_1: mark_2, player_2: mark_1})
            print(f'{player_1} chose "{mark_2}". {player_2} got "{mark_1}"\n')
            # current_player.update({'Player': player_1})
            score.update({player_1: default_score, player_2: default_score})
            break
        else:
            print(f'Input must be 1 for "{mark_1}" or 2 for "{mark_2}".')


# draws the mark into the board
def draw_player_mark(player, spots, players, mark_1, mark_2):
    while True:
        move = input(
            f'It\'s {player}\'s turn. Choose the spot according to a number between 1-9 or hit "q" to end the game: ')

        # if 'q' then returns the move to end the game
        if move == 'q':
            return move
        elif move.isdigit() and int(move) in spots:  # if str is a number
            move = int(move)  # turns str into int
            player_move = spots[move]
            player_mark = players[player]  # mark_1 or mark_2
            # if the chosen spot is already filled with mark_1 or mark_2, than asks for another spot
            if player_move == mark_1 or player_move == mark_2:
                print('Spot already filled. Choose again.')
            else:
                # updates the board according to the current player's move
                spots[move] = player_mark
                print('\n')
                break
        else:
            print('Input must be a number between 1 and 9.')


# checks if there's a winner
def check_for_win(spots):
    # horizontal check
    if (spots[1] == spots[2] == spots[3]) \
            or (spots[4] == spots[5] == spots[6]) \
            or (spots[7] == spots[8] == spots[9]):
        return True
    # vertical check
    elif (spots[1] == spots[4] == spots[7]) \
            or (spots[2] == spots[5] == spots[8]) \
            or (spots[3] == spots[6] == spots[9]):
        return True
    # diagonal check
    elif (spots[1] == spots[5] == spots[9]) \
            or (spots[3] == spots[5] == spots[7]):
        return True
    else:
        return False

# asks if the game continues
def continue_playing_question():
    while True:
        answer = input('Continue playing? 1 - yes / 2 - no: ')
        if answer == '1' or answer == '2':
            return answer
        else:
            print('Input must be 1 for "yes" or 2 for "no".')


# if win then shows msg
def win_msg(player_1, player_2, player, score):
    score_player_1, score_player_2 = score[player_1], score[player_2]

    if score_player_1 > score_player_2:
        print(f'{player_1} wins with a score of {score_player_1}\n'
              f'{player_2} looses with a score of {score_player_2}\n')
    elif score_player_1 < score_player_2:
        print(f'{player_2} wins with a score of {score_player_2}\n'
              f'{player_1} looses with a score of {score_player_1}\n')
    else:
        print(f'{player} won the the game, but the match ended in a tie.\n')
        print(f'{player_1} and {player_2} have {score_player_1} points\n')


# if tie then shows msg
def tie_msg(player_1, player_2, score, spots):
    score_player_1, score_player_2 = score[player_1], score[player_2]

    draw_board(spots)
    # if tie
    if score_player_1 == score_player_2:
        print('The game ended in a tie.\n'
              f'{player_1} and {player_2} have {score_player_1} points.\n')
    # if game ended in a tie but player 1 has more points
    elif score_player_1 > score_player_2:
        print(f'The game ended in a tie, but {player_1} made {score_player_1} points and is the winner of the match.\n'
              f'{player_2} made {score_player_2} points.\n')
    # if game ended in a tie but player 2 has more points
    else:
        print(f'The game ended in a tie, but {player_2} made {score_player_2} points and is the winner of the match.\n'
              f'{player_1} made {score_player_1} points.\n')



