from ..move import Move
from ..constants import KNIGHT_OFFSET
from .helpers import index_to_square, square_to_index, is_on_the_board, get_piece

def generate_knight_moves(game_state, square):
    board = game_state.board.board 
    side_to_move = game_state.side_to_move

    i, j = square_to_index(square)

    moves = []
    for x in KNIGHT_OFFSET:
        moves.append((i + x[0], j + x[1]))

    pseudo_legal_moves = []

    for move in moves:
        if is_on_the_board(*move):
            to_sq = index_to_square(*move)
            to_piece = get_piece(board, to_sq)
            if to_piece == '.':
                pseudo_legal_moves.append(Move(square, to_sq))
            elif side_to_move == 'w' and to_piece.islower():
                pseudo_legal_moves.append(Move(square, to_sq, is_capture = True))
            elif side_to_move == 'b' and to_piece.isupper():
                pseudo_legal_moves.append(Move(square, to_sq, is_capture = True))

    return pseudo_legal_moves
