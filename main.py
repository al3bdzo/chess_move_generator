from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_move
from src.move_applier import make_move


def main():
    state = GameState("8/8/8/pP6/8/8/8/8 w kq a6 0 1")
    moves = sorted(generate_pseudo_legal_move(state), key=lambda x: (x.from_sq, x.to_sq, x.promotion or ""))
    print(f"{state}\n")
    for move in moves:
        print(f"from: {move.from_sq}; to: {move.to_sq}")
    new_state = make_move(state, moves[0])
    print(f"{new_state}\n")
    


if __name__ == "__main__":
    main()
