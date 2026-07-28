from src.game_state import GameState
from src.move_validator import generate_legal_moves
from src.perft import perft
from src.move import Move

def main():
    state = GameState()
    
    for i in range(1, 5):
        print(f"perft({i}): {perft(state, i)}")
    
    kiwipete = GameState("r3k2r/p1ppqpb1/bn2pnp1/3PN3/1p2P3/2N2Q1p/PPPBBPPP/R3K2R w KQkq - 0 1")
    for i in range(1, 5):
        print(f"Kiwipete({i}): {perft(kiwipete, i)}")
    

if __name__ == "__main__":
    main()
