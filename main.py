from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_black_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_move


def main():
    state = GameState()
    moves = generate_pseudo_legal_move(state)
    print(f"{state}\n")
    print(f"number of moves: {len(moves)}")
    for move in moves:
        print(f"from: {move.from_sq}; to {move.to_sq}")
    


if __name__ == "__main__":
    main()
