from collections import Counter
import random
def player(prev_play, opponent_history=[]):
    if prev_play:
        opponent_history.append(prev_play)
    
    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    
    guess = random.choice(["R","S","P"])
    
    if len(opponent_history) >= 7:
        recent_moves = "".join(opponent_history[-7:])
        
        potential_moves = {'R': 0, 'P': 0, 'S': 0}
        for i in range(len(opponent_history) - 7):
            if "".join(opponent_history[i:i+7]) == recent_moves:
                if i + 7 < len(opponent_history):  # Ensure index is in bounds
                    next_move = opponent_history[i+7]
                    potential_moves[next_move] += 1
        
        predicted_move = max(potential_moves, key=potential_moves.get)
        guess = ideal_response[predicted_move]
    
    return guess
