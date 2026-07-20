from ..move import Move
from ..constants import QUEEN_DIRECTIONS, ROOK_DIRECTIONS, BISHOP_DIRECTIONS, KNIGHT_OFFSET, KING_OFFSET
from .helpers import square_to_index, is_on_the_board, index_to_square, get_piece, can_capture

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
            raise ValueError(f"Invalid piece passed!: {piece}")

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
                if can_capture(piece, to_piece):
                    moves.append(Move(square, to_sq, is_capture = True))
                    break
            else:
                break

    return moves
    

def generate_nk_moves(game_state, square):
    board = game_state.board.board 
    i, j = square_to_index(square)
    piece = get_piece(board, square)
    offset = []

    match piece.lower():
        case 'k':
            offset = KING_OFFSET
        case 'n':
            offset = KNIGHT_OFFSET
        case _:
            raise ValueError(f"Invalid piece passed!: {piece}")

    moves = []
    for di, dj in offset:
        moves.append((i + di, j + dj))

    pseudo_legal_moves = []

    for move in moves:
        if is_on_the_board(*move):
            to_sq = index_to_square(*move)
            to_piece = get_piece(board, to_sq)
            if to_piece == '.':
                pseudo_legal_moves.append(Move(square, to_sq))
            elif can_capture(piece, to_piece):
                pseudo_legal_moves.append(Move(square, to_sq, is_capture = True))

    return pseudo_legal_moves
