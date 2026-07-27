from .move_applier import make_move
from .move_validator import generate_legal_moves

def perft(state, depth):
    if depth == 0:
        return 1
    legal_moves = generate_legal_moves(state)
    nodes = 0
    for move in legal_moves:
        new_state = make_move(state, move)
        nodes += perft(new_state, depth - 1)
    return nodes