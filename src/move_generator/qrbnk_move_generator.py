from ..move import Move
from ..constants import QUEEN_DIRECTIONS, ROOK_DIRECTIONS, BISHOP_DIRECTIONS, KNIGHT_OFFSET, KING_OFFSET
from .helpers import square_to_index, is_on_the_board, index_to_square, get_piece

def generate_qrb_moves(game_state, square):
    board = game_state.board.board
    side_to_move = game_state.side_to_move
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

    for direction in directions:
        rank = i
        file = j 
        for _ in range(len(board)):
            rank = rank + direction[0]
            file = file + direction[1]
            if is_on_the_board(rank, file):
                to_sq = index_to_square(rank, file)
                to_piece = get_piece(board, to_sq)
                if to_piece == '.':
                    moves.append(Move(square, to_sq))
                    continue
                if side_to_move == 'w':
                    if to_piece.islower():
                        moves.append(Move(square, to_sq, is_capture = True))
                    break
                if side_to_move == 'b':
                    if to_piece.isupper():
                        moves.append(Move(square, to_sq, is_capture = True))
                    break
            else:
                break

    return moves
    

def generate_nk_moves(game_state, square):
    board = game_state.board.board 
    side_to_move = game_state.side_to_move

    i, j = square_to_index(square)
    piece = get_piece(board, square)
    offset = []

    match piece.lower():
        case 'k':
            offset = KING_OFFSET
        case 'n':
            offset = KNIGHT_OFFSET

    moves = []
    for x in offset:
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
