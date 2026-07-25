from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_moves
from src.move_applier import make_move
from src.game_rules import is_square_attacked, find_king, is_king_in_check
from src.move_validator import generate_legal_moves

def main():
    state = GameState()
    moves = generate_legal_moves(state)
    print(state)
    print()
    print(f"number of moves: {len(moves)}")
    for move in moves: 
        print(f"from: {move.from_sq}; to: {move.to_sq}")


if __name__ == "__main__":
    main()
