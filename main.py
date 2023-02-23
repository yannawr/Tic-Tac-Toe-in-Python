import random
import time
from helpers import register_player,  set_player_mark, show_score, draw_board, draw_player_mark, check_for_win, win_msg, continue_playing_question, tie_msg

spots_default = {1: '1', 2: '2', 3: '3', 4: '4',
                 5: '5', 6: '6', 7: '7', 8: '8', 9: '9'}

spots = spots_default.copy()

mark_1, mark_2 = 'X', 'O'

players = {}
current_player = {}
score = {}
turn = 1
playing = True

if __name__ == '__main__':
    while playing:
        # if no players, then register two players
        if not players:
            register_player(players)

            player_1, player_2 = list(players.keys())[
                0], list(players.keys())[1]

            # first player is chosen at random
            current_player['Player'] = random.choice(list(players.keys()))

            print('Setting the first player.')
            time.sleep(1)
            print('.')
            time.sleep(1)
            print('..')
            time.sleep(1)
            print('...')
            time.sleep(2)
            player = current_player['Player']
            print(f'The first player is: {player}\n')
            time.sleep(1)

            # sets mark_1 or mark_2 for each player
            set_player_mark(player_1, player_2, player, mark_1, mark_2, players, score)

        # sets the current player for when there are already registered players
        # (next rounds after the first one)
        player = current_player['Player']

        show_score(player_1, player_2, score)
        draw_board(spots)

        # if player hits 'q' then ends the game
        if draw_player_mark(player, spots, players, mark_1, mark_2) == 'q':
            playing = False

        # sets next player
        for i in players:
            if i != player:
                next_player = i

        if check_for_win(spots):
            current_player_score = score[player] + 1
            score[player] = current_player_score

            win_msg(player_1, player_2, player, score)
            if continue_playing_question() == '2':
                playing = False
            else:
                turn = 1
                next_player = player  # the winner has advantage and continues playing
                spots.clear()
                spots = spots_default.copy()

        # add the next turn to define if it's a tie
        # if turn > 9 and there's no winner in this turn, than there are not possible moves left next turn
        turn += 1
        if turn > 9:
            tie_msg(player_1, player_2, score, spots)

            if continue_playing_question() == '2':
                playing = False
            else:
                turn = 1
                spots.clear()
                spots = spots_default.copy()

        # calls next player
        current_player['Player'] = next_player
