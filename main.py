from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_pawn_moves
from src.move_generator.move_generator import generate_pseudo_legal_moves
from src.move_applier import make_move
from src.game_rules import is_square_attacked, find_king, is_king_in_check
from src.move_validator import generate_legal_moves
from src.perft import perft

def main():
    state = GameState("r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w - - 0 1")
    print(state)
    

if __name__ == "__main__":
    main()
