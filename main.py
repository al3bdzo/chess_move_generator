from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_move
from src.move_applier import make_move
from src.game_rules import is_square_attacked, find_king, is_king_in_check


def main():
    state = GameState()
    king_square = is_king_in_check(state, 'b')
    print(king_square)
    # moves = generate_pseudo_legal_move(state)
    # print(state)
    # for move in moves: 
    #     print(f"from: {move.from_sq}; to: {move.to_sq}")


if __name__ == "__main__":
    main()
