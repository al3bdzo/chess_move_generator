from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_moves
from src.move_generator.qrbnk_move_generator import handle_castling
from src.move_applier import make_move
from src.game_rules import is_square_attacked, find_king, is_king_in_check
from src.move_validator import generate_legal_moves
from src.perft import perft
from src.move import Move

def main():
    state = GameState("4k3/8/8/8/8/8/2r2r2/R3K2R w KQ - 0 1")
    moves = handle_castling(state, "e1")
    print(state)

    for move in moves:
        print(f"from: {move.from_sq}; to: {move.to_sq}")
    

if __name__ == "__main__":
    main()
