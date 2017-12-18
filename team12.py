import random

team_name = 'Team 12'
strategy_name = 'BOONK GANG'
strategy_description = 'By their history'

import random


def move(my_history, their_history, my_score, their_score):     
    choice = random.choice(['a', 'm', 'o'])
    if len(their_history) == 0:
        return 'b'
    else:
        if choice == 'a':
            return advantage(their_history)
        if choice == 'm':
            return mimic(their_history)
        if choice == 'o':
            return odds(their_history)

def odds(their_history):
    choices = ['b','b','b','b','b','b','b','b','b','b','c','c','c','c','c','c','c','c','c''c']
    if their_history[-1] == 'b':
        return random.choice(choices[:15])
    elif their_history[-1] == 'c':
        return random.choice(choices[5:])
    
def advantage(their_history):
    if their_history[-1] == 'b':
        return 'b'
    if their_history[-1] == 'c':
        return 'b'
    if their_history[-1:0] == 'ccc'or 'bcb':
        return 'c'

def mimic(my_history, their_history):
    if my_history == 0:
        return 'c'
    else:
        return their_history[-1]