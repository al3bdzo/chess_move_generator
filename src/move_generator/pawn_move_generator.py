from ..move import Move
from ..constants import WHITE_PAWN_OFFSET, BLACK_PAWN_OFFSET
from .helpers import index_to_square, square_to_index, get_piece, is_on_the_board, is_rank, is_double_pawn_push, can_capture


def generate_pawn_moves(game_state, square):
    board = game_state.board.board
    en_passant_square = game_state.en_passant_square
    piece = get_piece(board, square)
    psuedo_legal_moves = []

    i, j = square_to_index(square)

    match piece:
        case 'p':
            offset = BLACK_PAWN_OFFSET
            promotions = ['r', 'n', 'b', 'q']
            home_rank_index = 1
            promotion_rank_index = 6
        case 'P':
            offset = WHITE_PAWN_OFFSET
            promotions = ['R', 'N', 'B', 'Q']
            home_rank_index = 6
            promotion_rank_index = 1
        case _:
            raise ValueError(f"Unexpected piece passed: {piece}")

    for di, dj in offset:
        rank = i + di
        file = j + dj
        if is_on_the_board(rank, file):
            to_sq = index_to_square(rank, file)
            to_piece = get_piece(board, to_sq)

            if is_rank(i, home_rank_index) and is_double_pawn_push(board, i, j, rank, file):
                psuedo_legal_moves.append(Move(square, to_sq, is_double_pawn_push = True))
                continue

            if to_piece == '.' and dj == 0 and abs(di) == 1: 
                if is_rank(i, promotion_rank_index):
                    for promotion in promotions:
                        psuedo_legal_moves.append(Move(square, to_sq, promotion))
                else:
                    psuedo_legal_moves.append(Move(square, to_sq))
                continue

            if can_capture(piece, to_piece) and dj != 0:
                if is_rank(i, promotion_rank_index):
                    for promotion in promotions:
                        psuedo_legal_moves.append(Move(square, to_sq, promotion, is_capture = True))
                else:
                    psuedo_legal_moves.append(Move(square, to_sq, is_capture = True))
                continue

            if to_sq == en_passant_square and dj != 0:
                psuedo_legal_moves.append(Move(square, to_sq, is_capture = True, is_en_passant = True))

    return psuedo_legal_moves