from ..move import Move
from .pawn_move_generator import generate_pawn_moves
from .helpers import index_to_square, square_to_index
from .qrbn_move_generator import generate_qrb_moves, generate_knight_moves
from .king_move_generator import generate_king_moves

def generate_pseudo_legal_move(game_state):
    board = game_state.board.board
    side_to_move = game_state.side_to_move
    en_passant_square = game_state.en_passant_square
    moves = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            piece = board[i][j]
            square = index_to_square(i, j)
            match piece:
                case 'K':
                    moves.extend(generate_king_moves(game_state, square))
                case 'k':
                    moves.extend(generate_king_moves(game_state, square))


    return moves