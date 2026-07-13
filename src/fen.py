from .game_state import GameState
from .board import Board

def parse_fen(fen):
    fen_parts = fen.split()
    if len(fen_parts) != 6:
        raise ValueError("Invalid FEN: expected 6 fields")

    board = Board(fen_parts[0])
    gameState = GameState(board, fen_parts[1], fen_parts[2], fen_parts[3], fen_parts[4], fen_parts[5])
    return gameState

