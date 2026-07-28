from .move_applier import make_move_in_place, undo_move
from .move_validator import generate_legal_moves

def perft(state, depth):
    if depth == 0:
        return 1
    nodes = 0

    for move in generate_legal_moves(state):
        undo = make_move_in_place(state, move)
        nodes += perft(state, depth - 1)
        undo_move(state, move, undo)

    return nodes