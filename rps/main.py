import random

def player(prev_play, opponent_history=[]):
    # Save the opponent's last move
    if prev_play:
        opponent_history.append(prev_play)

    # For first few moves, just return 'R'
    if len(opponent_history) < 5:
        return 'R'

    # === Pattern Matching ===
    # Use a sliding window of the last 3 moves to predict next move
    recent = "".join(opponent_history[-3:])
    patterns = {}

    # Build a pattern database from history
    for i in range(len(opponent_history) - 3):
        pattern = "".join(opponent_history[i:i+3])
        next_move = opponent_history[i+3]
        if pattern not in patterns:
            patterns[pattern] = {"R": 0, "P": 0, "S": 0}
        patterns[pattern][next_move] += 1

    # Predict opponent's next move based on matching pattern
    if recent in patterns:
        prediction = max(patterns[recent], key=patterns[recent].get)
    else:
        # Fallback: Frequency analysis
        freq = {"R": 0, "P": 0, "S": 0}
        for move in opponent_history:
            freq[move] += 1
        prediction = max(freq, key=freq.get)

    # Play the counter to the predicted move
    counter_moves = {"R": "P", "P": "S", "S": "R"}
    return counter_moves[prediction]

