team_name = 'TEAM 6'
strategy_name = 'Free Points, You Can Trust Us'
strategy_description = 'Mostly Collude'

def move(my_history, their_history, my_score, their_score) :
    if len(my_history) <= 5:
        return 'c'
    if their_history == 'b' :
        return 'c'
    if their_history == 'c' :
        return 'c'
    if their_history == ['c','c','c'] :
        return 'b'
    if their_score < my_score :
        return 'c'
    
