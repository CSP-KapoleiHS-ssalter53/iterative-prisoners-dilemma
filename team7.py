team_name = 'team 7'
strategy_name = 'Hopscotch'
strategy_description = 'Betray/collude alterantes every five rounds, betray/collude if in the last 5 rounds opponent colludes/betrays more than three times.' 

import random
def move(my_history,their_history, my_score, their_score):
    if len(my_history)==0:
        return 'b'


    if len(my_history)==1:
        return 'b'
    if len(my_history)==2:
        return 'b'
    if len(my_history)==3: 
        return 'c'
        
        
    b=0
    for move in their_history[-5:]:
        if move =='b':
            b += 1
        if b>=3:
            return 'b'
        elif b<=2:
                return 'c'
    c=0
    for move in their_history[-5:]:
        if move =='c':
            c += 1
        if c>=3:
            return 'c'
        elif c<=2:
            return 'b'
    
    
    if len(my_history)==4:
        return 'b'
    if len(my_history)==9:
        return 'c'
    if len(my_history)==14:
        return 'b'
    if len(my_history)==19:
        return 'c'
    if len(my_history)==24:
        return 'b'
    if len(my_history)==29:
        return 'c'
    if len (my_history)==34:
        return 'b'
    if len(my_history)==39:
        return 'c'
    if len(my_history)==44:
        return 'c'
    if len(my_history)==49:
        return 'b'
    if len(my_history)==54:
        return 'c'
    if len (my_history)==59:
        return 'b'
    if len(my_history)==64:
        return 'c'
    if len(my_history)==69:
        return 'b'
    if len(my_history)==74:
        return 'c'
    if len (my_history)==79:
        return 'b'
    if len(my_history)==84:
        return 'c'
    if len (my_history)==89:
        return 'b'
    if len(my_history)==94:
        return 'c'
    if len (my_history)==99:
        return 'b'
    
    if random.random()<0.2:
        return 'b'
