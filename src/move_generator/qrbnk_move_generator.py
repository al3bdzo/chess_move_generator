from ..move import Move
from ..constants import QUEEN_DIRECTIONS, ROOK_DIRECTIONS, BISHOP_DIRECTIONS, KNIGHT_OFFSET, KING_OFFSET
from .helpers import square_to_index, is_on_the_board, index_to_square, get_piece, can_capture, check_empty_squares, check_attacked_squares

def generate_qrb_moves(game_state, square):
    board = game_state.board.board
    moves = []
    i, j = square_to_index(square)
    piece = get_piece(board, square)
    directions = []

    match piece.lower():
        case 'q':
            directions = QUEEN_DIRECTIONS
        case 'r':
            directions = ROOK_DIRECTIONS
        case 'b':
            directions = BISHOP_DIRECTIONS
        case _:
            raise ValueError(f"Invalid piece passed!: {piece}; expected: (q, r, b)")

    for direction in directions:
        rank = i
        file = j 
        while True:
            rank = rank + direction[0]
            file = file + direction[1]
            if is_on_the_board(rank, file):
                to_sq = index_to_square(rank, file)
                to_piece = get_piece(board, to_sq)
                if to_piece == '.':
                    moves.append(Move(square, to_sq))
                    continue
                elif can_capture(piece, to_piece):
                    moves.append(Move(square, to_sq, is_capture = True))
                    break
                else:
                    break
            else:
                break

    return moves
    

def handle_castling(game_state, square):
    castling_moves = []

    side_to_move = game_state.side_to_move
    board = game_state.board.board
    wk, wq, bk, bq = game_state.get_castling_rights()

    if side_to_move == 'w':
        if square != 'e1':
            return []
        king = 'K'
        rook = 'R'
        rook_king = 'h1'
        rook_queen = 'a1'

        king_side_empty = ['f1', 'g1']
        king_side_attacked = ['f1', 'g1', 'e1']

        queen_side_empty = ['b1', 'c1', 'd1']
        queen_side_attacked = ['c1', 'd1', 'e1']

        attacker = 'b'

        to_square_ks = 'g1'
        to_square_qs = 'c1'
        ks = wk
        qs = wq
    
    else:
        if square != 'e8':
            return []
        king = 'k'
        rook = 'r'
        rook_king = 'h8'
        rook_queen = 'a8'

        king_side_empty = ['f8', 'g8']
        king_side_attacked = ['f8', 'g8', 'e8']

        queen_side_empty = ['b8', 'c8', 'd8']
        queen_side_attacked = ['c8', 'd8', 'e8']

        attacker = 'w'

        to_square_ks = 'g8'
        to_square_qs = 'c8'
        ks = bk
        qs = bq

    if get_piece(board, square) == king:
        if ks:
            if get_piece(board, rook_king) == rook:
                if check_empty_squares(board, king_side_empty) and check_attacked_squares(game_state, king_side_attacked, attacker):
                    castling_moves.append(Move(square, to_square_ks, is_castling = True))
        if qs:
            if get_piece(board, rook_queen) == rook:
                if check_empty_squares(board, queen_side_empty) and check_attacked_squares(game_state, queen_side_attacked, attacker):
                    castling_moves.append(Move(square, to_square_qs, is_castling = True))

    return castling_moves


def generate_nk_moves(game_state, square):
    board = game_state.board.board 
    i, j = square_to_index(square)
    piece = get_piece(board, square)
    offset = []
    pseudo_legal_moves = []

    match piece.lower():
        case 'k':
            offset = KING_OFFSET
            pseudo_legal_moves.extend(handle_castling(game_state, square))
        case 'n':
            offset = KNIGHT_OFFSET
        case _:
            raise ValueError(f"Invalid piece passed!: {piece}; expected: (n, k)")


    for di, dj in offset:
        move = (i + di, j + dj)
        if is_on_the_board(*move):
            to_sq = index_to_square(*move)
            to_piece = get_piece(board, to_sq)
            if to_piece == '.':
                pseudo_legal_moves.append(Move(square, to_sq))
            elif can_capture(piece, to_piece):
                pseudo_legal_moves.append(Move(square, to_sq, is_capture = True))

    return pseudo_legal_moves
