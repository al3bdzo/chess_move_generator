import copy
from .move_generator.helpers import index_to_square, square_to_index, get_piece

def make_move(state, move):
    new_state = copy.deepcopy(state)

    old_board = state.board.board
    new_board = new_state.board.board

    side_to_move = state.side_to_move
    forward = 1

    from_rank, from_file = square_to_index(move.from_sq)
    to_rank, to_file = square_to_index(move.to_sq)
    to_piece = get_piece(old_board, move.to_sq)

    if move.promotion is None:
        new_board[to_rank][to_file] = get_piece(old_board, move.from_sq)
    else:
        new_board[to_rank][to_file] = move.promotion
    
    new_board[from_rank][from_file] = '.'

    if side_to_move == 'w':
        new_state.side_to_move = 'b'
        forward = -1 
    else:
        new_state.side_to_move = 'w'
    
    if move.is_en_passant:
        new_board[to_rank - forward][to_file] = '.'

    if move.is_double_pawn_push:
        new_state.en_passant_square = index_to_square(from_rank + forward, from_file)
    else: 
        new_state.en_passant_square = '-'

    # don't forget: castling rights, half move and full move counters, 
    if state.castling_rights != '-':
        wk, wq, bk, bq = state.get_castling_rights()
        if move.from_sq == "e1":
            wk = False
            wq = False
        if move.from_sq == "h1":
            wk = False
        if move.from_sq == "a1":
            wq = False
        if move.to_sq == "h8" and move.is_capture == True and to_piece == 'r':
            bk = False
        if move.to_sq == "a8" and move.is_capture == True and to_piece == 'r':
            bq = False

        if move.from_sq == "e8":
            bk = False
            bq = False
        if move.from_sq == "h8":
            bk = False
        if move.from_sq == "a8":
            bq = False
        if move.to_sq == "h1" and move.is_capture == True and to_piece == 'R':
            wk = False
        if move.to_sq == "a1" and move.is_capture == True and to_piece == 'R':
            wq = False
        
        new_state.set_castling_right(wk, wq, bk, bq)
    
    if move.is_castling:
        if move.from_sq == "e1":
            if move.to_sq == "g1":
                i, j = square_to_index("h1")
                new_board[i][j] = '.'
                i, j = square_to_index("f1")
                new_board[i][j] = 'R'
            if move.to_sq == "c1":
                i, j = square_to_index("a1")
                new_board[i][j] = '.'
                i, j = square_to_index("d1")
                new_board[i][j] = 'R'
        if move.from_sq == "e8":
            if move.to_sq == "g8":
                i, j = square_to_index("h8")
                new_board[i][j] = '.'
                i, j = square_to_index("f8")
                new_board[i][j] = 'r'
            if move.to_sq == "c8":
                i, j = square_to_index("a8")
                new_board[i][j] = '.'
                i, j = square_to_index("d8")
                new_board[i][j] = 'r'

    return new_state


def undo_move(state, move):
    pass