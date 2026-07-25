import copy
from .move_generator.helpers import index_to_square, square_to_index, get_piece

def make_move(state, move):
    new_state = copy.deepcopy(state)

    old_board = state.board.board
    new_board = new_state.board.board

    side_to_move = state.side_to_move
    en_passant_square_rank = 1

    from_rank, from_file = square_to_index(move.from_sq)
    to_rank, to_file = square_to_index(move.to_sq)

    if move.promotion is None:
        new_board[to_rank][to_file] = get_piece(old_board, move.from_sq)
    else:
        new_board[to_rank][to_file] = move.promotion
    
    new_board[from_rank][from_file] = '.'

    if side_to_move == 'w':
        new_state.side_to_move = 'b'
        en_passant_square_rank = -1 
    else:
        new_state.side_to_move = 'w'
    
    if move.is_en_passant:
        new_board[to_rank - en_passant_square_rank][to_file] = '.'

    if move.is_double_pawn_push:
        new_state.en_passant_square = index_to_square(from_rank + en_passant_square_rank, from_file)
    else: 
        new_state.en_passant_square = '-'

    return new_state


def undo_move(state, move):
    pass