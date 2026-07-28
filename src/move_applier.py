import copy
from .move_generator.helpers import index_to_square, square_to_index, get_piece
from .move import UndoInfo

def make_move(state, move):
    new_state = copy.deepcopy(state)

    old_board = state.board.board
    new_board = new_state.board.board

    side_to_move = state.side_to_move
    forward = 1

    from_rank, from_file = square_to_index(move.from_sq)
    to_rank, to_file = square_to_index(move.to_sq)
    to_piece = get_piece(old_board, move.to_sq)
    moving_piece = get_piece(old_board, move.from_sq)

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
        new_state.full_move_number += 1
    
    if move.is_en_passant:
        new_board[to_rank - forward][to_file] = '.'

    if move.is_double_pawn_push:
        new_state.en_passant_square = index_to_square(from_rank + forward, from_file)
    else: 
        new_state.en_passant_square = '-'

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
    
    if moving_piece.lower() == 'p' or move.is_capture:
        new_state.halfmove_clock = 0
    else:
        new_state.halfmove_clock += 1

    return new_state


def make_move_in_place(state, move):
    board = state.board.board

    from_rank, from_file = square_to_index(move.from_sq)
    to_rank, to_file = square_to_index(move.to_sq)

    moving_piece = board[from_rank][from_file]
    captured_piece = board[to_rank][to_file]

    undo = UndoInfo(
        captured_piece=captured_piece,
        castling_rights=state.castling_rights,
        en_passant_square=state.en_passant_square,
        halfmove_clock=state.halfmove_clock,
        full_move_number=state.full_move_number,
    )

    forward = -1 if state.side_to_move == "w" else 1

    board[from_rank][from_file] = '.'

    if move.promotion is None:
        board[to_rank][to_file] = moving_piece
    else:
        board[to_rank][to_file] = move.promotion

    if move.is_en_passant:
        board[to_rank - forward][to_file] = '.'

    if move.is_castling:

        if move.from_sq == "e1" and move.to_sq == "g1":
            board[7][7] = '.'
            board[7][5] = 'R'

        elif move.from_sq == "e1" and move.to_sq == "c1":
            board[7][0] = '.'
            board[7][3] = 'R'

        elif move.from_sq == "e8" and move.to_sq == "g8":
            board[0][7] = '.'
            board[0][5] = 'r'

        elif move.from_sq == "e8" and move.to_sq == "c8":
            board[0][0] = '.'
            board[0][3] = 'r'

    if state.side_to_move == "w":
        state.side_to_move = "b"
    else:
        state.side_to_move = "w"
        state.full_move_number += 1

    if moving_piece.lower() == "p" or move.is_capture:
        state.halfmove_clock = 0
    else:
        state.halfmove_clock += 1

    if move.is_double_pawn_push:
        state.en_passant_square = index_to_square(
            from_rank + forward,
            from_file
        )
    else:
        state.en_passant_square = "-"

    return undo


def undo_move(state, move, undo):
    board = state.board.board

    from_rank, from_file = square_to_index(move.from_sq)
    to_rank, to_file = square_to_index(move.to_sq)

    moved_piece = board[to_rank][to_file]

    if state.side_to_move == "w":
        state.side_to_move = "b"
    else:
        state.side_to_move = "w"

    state.castling_rights = undo.castling_rights
    state.en_passant_square = undo.en_passant_square
    state.halfmove_clock = undo.halfmove_clock
    state.full_move_number = undo.full_move_number

    if move.is_castling:

        if move.from_sq == "e1" and move.to_sq == "g1":
            board[7][5] = '.'
            board[7][7] = 'R'

        elif move.from_sq == "e1" and move.to_sq == "c1":
            board[7][3] = '.'
            board[7][0] = 'R'

        elif move.from_sq == "e8" and move.to_sq == "g8":
            board[0][5] = '.'
            board[0][7] = 'r'

        elif move.from_sq == "e8" and move.to_sq == "c8":
            board[0][3] = '.'
            board[0][0] = 'r'

    if move.promotion is not None:

        if state.side_to_move == "w":
            board[from_rank][from_file] = "P"
        else:
            board[from_rank][from_file] = "p"

    else:
        board[from_rank][from_file] = moved_piece

    if move.is_en_passant:

        board[to_rank][to_file] = '.'

        if state.side_to_move == "w":
            board[to_rank + 1][to_file] = 'p'
        else:
            board[to_rank - 1][to_file] = 'P'

    else:
        board[to_rank][to_file] = undo.captured_piece