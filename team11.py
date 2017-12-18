import random 
team_name = 'team11'
strategy_name = 'SneakyBastartd+Crook/BullesyeAce+Armorer'
strategy_description = 'Yeet'
def move(my_history, their_history, my_score, their_score): #Startegy name: The legend 28
    if len(my_history) == 0:
        return 'c' #Returns Collude on the first round
    elif my_history[-1:101]=='c' and their_history[-1:101] =='b': #If they betray we betray the next round.
        return 'b'
    else:
        return 'c'
    if their_history == 'cc':
        return 'b'
    if my_history % 5 == 0: 
        return random.choice(['b','c'])
