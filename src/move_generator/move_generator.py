from ..move import Move
from .pawn_move_generator import generate_white_pawn_moves, generate_black_pawn_moves
from .helpers import index_to_square, square_to_index


def generate_pseudo_legal_move(game_state):
    board = game_state.board.board
    side_to_move = game_state.side_to_move
    en_passant_square = game_state.en_passant_square
    moves = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            piece = board[i][j]
            square = index_to_square(i, j)
            if side_to_move == 'w':
                match piece:
                    case '.':
                        continue
                    case 'P':
                        moves.extend(generate_white_pawn_moves(game_state, square))
            elif side_to_move == 'b':
                match piece:
                    case '.':
                        continue
                    case 'p':
                        moves.extend(generate_black_pawn_moves(game_state, square))

    return moves