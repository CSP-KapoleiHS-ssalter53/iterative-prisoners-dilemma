team_name = 'team3'
strategy_name = 'Conditions'
strategy_description ='Uses conditions to decide the next move.'

import random

def move(my_history, their_history, my_score, their_score):

    if my_history==0:
        return 'b' #Betray First round
        
    for my_history in range(-5):
        return random.choice['c','b']

    if their_score<=my_score:
        return 'c'
        
    if their_score>=my_score:
        return 'b'
            
    if their_score==my_score:
        return 'c' 