from .board import Board

class GameState:
    def __init__(self, fen = None):
        self.fen = fen
        self.board = Board()
        self.side_to_move = 'w'
        self.castling_rights = '-'
        self.en_passant_square = '-'
        self.halfmove_clock = 0
        self.full_move_number = 0

        if self.fen:
            self.build_from_fen()

    def build_from_fen(self):
        if self.fen == None:
            return 
        
        fen_parts = self.fen.split()
        if len(fen_parts) != 6:
            raise ValueError("Invalid FEN: expected 6 fields")

        self.board = Board(fen_parts[0])
        self.side_to_move = fen_parts[1]
        self.castling_rights = fen_parts[2]
        self.en_passant_square = fen_parts[3]
        self.halfmove_clock = fen_parts[4]
        self.full_move_number = fen_parts[5]
    
    def __repr__(self):
        representation = f"{repr(self.board)}"
        representation += f"side to move: {self.side_to_move}\n"
        representation += f"castling right: {self.castling_rights}\n"
        representation += f"en_passant square: {self.en_passant_square}\n"
        representation += f"halfmove clock: {self.halfmove_clock}\n"
        representation += f"full move number: {self.full_move_number}"
        return representation