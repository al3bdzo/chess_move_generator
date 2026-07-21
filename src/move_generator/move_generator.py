from ..move import Move
from .pawn_move_generator import generate_pawn_moves
from .helpers import index_to_square, square_to_index
from .qrbnk_move_generator import generate_qrb_moves, generate_nk_moves

def generate_pseudo_legal_move(game_state):
    board = game_state.board.board
    moves = []
    side_to_move = game_state.side_to_move

    for i in range(len(board)):
        for j in range(len(board[i])):
            piece = board[i][j]
            square = index_to_square(i, j)
            if side_to_move == 'w' and piece == 'P':
                moves.extend(generate_pawn_moves(game_state, square))
            if side_to_move == 'b' and piece == 'p':
                moves.extend(generate_pawn_moves(game_state, square))

    return moves