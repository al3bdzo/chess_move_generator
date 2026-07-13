from src.fen import parse_fen
from src.game_state import GameState

def main():
    state = parse_fen("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1")
    print(state)


if __name__ == "__main__":
    main()
