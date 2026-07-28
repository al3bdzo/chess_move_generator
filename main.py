from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_moves
from src.move_applier import make_move
from src.game_rules import is_square_attacked, find_king, is_king_in_check
from src.move_validator import generate_legal_moves
from src.perft import perft
from src.move import Move

def main():
    state = GameState("r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1")
    move = Move("a1", "a8", is_capture = True)
    new_state = make_move(state, move)
    print(new_state)
    

if __name__ == "__main__":
    main()
