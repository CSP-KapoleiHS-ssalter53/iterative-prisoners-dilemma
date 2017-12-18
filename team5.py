team_name = 'TEAM 5'
strategy_name = 'Winning Strategy'
strategy_description = 'Random for first 5 turns, counter for 10, betray for the rest'

import random
def move(my_history, their_history, my_score, their_score):
    if len(my_history) <= 5:
        firstturns = random.choice('c''b')
        return firstturns
    bcount = 0
    for letter in their_history[-5:-1]:
        if letter == 'b':
            bcount += 1
            if bcount >= 2:
                return 'b'
    else:
        return 'c'
    if len(my_history) >= 10:
        return 'b'