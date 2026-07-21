from ..move import Move
from .pawn_move_generator import generate_pawn_moves
from .helpers import index_to_square, square_to_index, get_piece
from .qrbnk_move_generator import generate_qrb_moves, generate_nk_moves

def generate_pseudo_legal_move(game_state):
    board = game_state.board.board
    moves = []
    side_to_move = game_state.side_to_move
    for i in range(8):
        for j in range(8):
            square = index_to_square(i, j)
            piece = get_piece(board, square)
            if side_to_move == 'w':
                match(piece):
                    case 'P':
                        moves.extend(generate_pawn_moves(game_state, square))
                    case 'N' | 'K':
                        moves.extend(generate_nk_moves(game_state, square))
                    case 'Q' | 'B' | 'R':
                        moves.extend(generate_qrb_moves(game_state, square))
            elif side_to_move == 'b':
                match(piece):
                    case 'p':
                        moves.extend(generate_pawn_moves(game_state, square))
                    case 'n' | 'k':
                        moves.extend(generate_nk_moves(game_state, square))
                    case 'q' | 'r' | 'b':
                        moves.extend(generate_qrb_moves(game_state, square))
    return moves