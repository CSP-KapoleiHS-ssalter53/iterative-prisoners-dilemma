team_name = 'team8'
strategy_name = 'APavlov'
strategy_description = 'Copy opponents last move if opponent is cooperative, betray if oppontent is mostly betraying'

def move(my_history, their_history, my_score, their_score):
    if len(my_history) == 0:
        return 'c'
    elif len(their_history) < 7:
        return len(their_history[-1])
    b=0
    c=0
    for move in their_history[-6:len(their_history)]:
            if move == 'b':
                b += 1
            if move == 'c':
                c += 1
            if c >= 3:
                return len(their_history[-1])
            elif b >= 4:
                return 'b'
            else:
                return 'b'
