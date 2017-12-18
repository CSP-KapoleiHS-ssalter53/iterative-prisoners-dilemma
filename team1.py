###
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Team 1' # Only 10 chars displayed.
strategy_name = 'follow the leader'
strategy_description = 'i see your b and raise you a c'
    

   
def move(my_history, their_history, my_score, their_score):
    ''' Arguments accepted: my_history, their_history are strings.
    my_score, their_score are ints.'''
       
    if len(my_history) == 0:
        return 'c'
    elif 'b' in (their_history[-2:]):
        return 'b'
    else:
        return 'c'