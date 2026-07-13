from .board import Board

class GameState:
    def __init__(
            self, 
            board = Board(), 
            side_to_move = 'w', 
            castling_rights = '-', 
            en_passant_square = '-', 
            halfmove_clock = 0, 
            full_move_number = 0
        ):

        self.board = board
        self.side_to_move = side_to_move
        self.en_passant_square = en_passant_square
        self.halfmove_clock = halfmove_clock
        self.full_move_number = full_move_number

    
    def __repr__(self):
        representation = f"{repr(self.board)}"
        representation += f"side to move: {self.side_to_move}\n"
        representation += f"en_passant_square: {self.en_passant_square}\n"
        representation += f"halfmove clock: {self.halfmove_clock}\n"
        representation += f"full_move_number: {self.full_move_number}"
        return representation