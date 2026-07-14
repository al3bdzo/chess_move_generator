from src.fen import parse_fen
from src.game_state import GameState
from src.move_generator import generate_pawn_moves

def main():
    state = GameState("8/8/8/8/3p1p2/8/4P3/8 w - - 0 1")
    print(f"{state}\n")
    


if __name__ == "__main__":
    main()
