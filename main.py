from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_move


def main():
    state = GameState("8/8/8/8/4pP2/8/8/8 b - f3 0 1")
    moves = sorted(generate_pseudo_legal_move(state), key=lambda x: (x.from_sq, x.to_sq, x.promotion or ""))
    print(f"{state}\n")
    print(f"number of moves: {len(moves)}")
    for move in moves:
        print(f"from: {move.from_sq}; to {move.to_sq}; is_capture: {move.is_en_passant}")
    


if __name__ == "__main__":
    main()
