team_name = 'Team1000'
strategy_name = 'Su-wiiiipe.'
strategy_description = 'Su-wiiiiiiiiiiiiiiiipe.'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    # This player always colludes.
    return 'c'
def pro_strats(my_history, their_history, my_score, their_score):
    if my_score==0:
         if 'c' in my_history[-1]:
            return 'c'
         else: 
            return 'b'
    else:
        while my_score<their_score:
            if 'c' in their_history[-1]:
                return 'b'
            elif 'b' in their_history[-5:-1]:
                return 'c'
    while their_score<my_score:
        if 'c' in their_history[-2:-1]:
            return 'b'
        else:
            return'c'
    while my_score==their_score:
        if 'c' in my_history[-1]:
            return 'b'
        else: 
            return 'c'
            