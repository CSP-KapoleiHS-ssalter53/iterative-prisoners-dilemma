import random 
team_name = 'team13' # Only 10 chars displayed.
strategy_name = 'win'
strategy_description = 'beat other teams'
    
def move(my_history, their_history, my_score, their_score):
    if len(my_history)==0:
        return 'b'
    else:
         recent_round_them = their_history[-1]
         recent_round_me = my_history[-1]
         for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
        
            if (prior_round_me == 'b') and \
                    (prior_round_them == 'c'):
                return random.choice(['c','b'])
            if (prior_round_me == recent_round_them) and (prior_round_them == recent_round_me):
                return 'b'
                        
