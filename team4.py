####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 4'
strategy_name = 'Mr.Mime'
strategy_description = 'Betray the first and last 5 turns, copy the opponets last move for the rest'
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    
    if len(my_history) == 0: # look for length of my history = 0
        return 'b' #First round
    if their_history =='ccc':
        return 'b'
    elif len(my_history) >= 95:
            return 'b'
    else:
        return their_history[-1]
 
    
     
    # return 'c' first move
   # if my_history'b' < their_history'b'
           # return 'b'
           # else return 'c'
           # if >95 answers have been given return b (first)
          