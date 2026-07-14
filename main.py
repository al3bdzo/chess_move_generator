from src.fen import parse_fen
from src.game_state import GameState
from src.move_generator import generate_pawn_moves

def main():
    state = GameState()
    moves = generate_pawn_moves(state)
    print(f"{state}\n")
    for move in moves:
        print(f"from: {move.from_sq}; to: {move.to_sq}")


if __name__ == "__main__":
    main()
