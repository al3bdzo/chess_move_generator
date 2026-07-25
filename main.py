from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_move
from src.move_applier import make_move
from src.game_rules import is_square_attacked


def main():
    state = GameState()
    
    is_attacked = is_square_attacked(state, "a3", "w")
    print(is_attacked)
    


if __name__ == "__main__":
    main()
