####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'MK' # Only 10 chars displayed.
strategy_name = 'Collude first 25 rounds unless betrayed. Betray 26th round forward.'
strategy_description = 'Betray if betrayed. If I did not betrayed yet, starting the 11th round, I betray.'

import random    
            
def move(my_history, their_history, my_score, their_score):
    '''Make move based off other player history
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray. 
    '''
    
    if len(my_history)== 0:
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    else:
        return 'c' #Until 26th round    
        
    #If 26th round
    if len(their_history)>25:
        return 'b'
        
        
    
      