from .move_generator.move_generator import generate_pseudo_legal_moves
from .game_rules import is_king_in_check
from .move_applier import make_move


def generate_legal_moves(game_state):
    pseudo_legal_moves = generate_pseudo_legal_moves(game_state)
    side = game_state.side_to_move
    legal_moves = []

    for move in pseudo_legal_moves:
        new_state = make_move(game_state, move)

        if not is_king_in_check(new_state, side):
            legal_moves.append(move)
    
    return legal_moves
