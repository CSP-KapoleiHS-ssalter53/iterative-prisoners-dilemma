import random

team_name = 'team 14'
strategy_name = 'Counter and Guess Random'
strategy_description = 'try to see their moves before they do it, and try to score as much points as possible with random guesses.'

def move(my_history, their_history, my_score, their_score):
    count = 0
    for letter in their_history[-10:-1]:
        if letter == 'b':
            count += 1
    if ((count/10) >= 0.5) or ((count/10) >= 0.3):
        return 'b'
    else:
        return random.choice(['b','c']) 
    if 'b' in their_history[-80:] >= 0.5:
        return 'b'
    else:
        return 'c'