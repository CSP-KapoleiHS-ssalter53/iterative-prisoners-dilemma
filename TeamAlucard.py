import random
team_name = 'Team Dracula'
strategy_name = 'The Mind Of An Immortal'
strategy_description = 'Older than mortal comprehension, no human can ever hope to understand such a being'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:        
        return strat(6, their_history, my_history)
        
    return strat(random.randint(1, 6), their_history, my_history)
def strat(secret, their_history, my_history):
    if secret == 1 :
        if 'b' in their_history:
            return 'b'
        else:
            return 'c'
   
    elif secret == 2 :
        if 'b' in their_history:
            return 'c'
        else:
            return 'b'
            
    elif secret == 3 : 
        if len(my_history)== 0:
            return 'c'
        else:
            return 'b'
            
    elif secret == 4 :
        if 'c' in my_history:
            return 'b'
        else:
            return 'c'
            
    elif secret == 5 :
        if 'b' in their_history[-1]:
            return 'b'
        else:
            return 'c'
            
    elif secret == 6 :
        return random.choice(['c', 'b'])