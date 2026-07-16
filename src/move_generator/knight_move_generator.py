from ..move import Move
from .helpers import index_to_square, square_to_index

def generate_knight_moves(game_state, square):
    board = game_state.board.board 
    side_to_move = game_state.side_to_move

    i, j = square_to_index(square)

    moves = [(i + 2, j + 1), (i + 2, j - 1), (i - 2, j + 1), (i - 2, j - 1), (i + 1, j - 2), (i - 1, j - 2), (i + 1, j + 2), (i - 1, j + 2)]
    pseudo_legal_moves = []

    for move in moves:
        if move[0] >= 0 and move[0] <= 7 and move[1] >= 0 and move[1] <= 7:
            to_sq = index_to_square(*move)
            if board[move[0]][move[1]] == '.':
                pseudo_legal_moves.append(Move(square, to_sq))
            if side_to_move == 'w' and board[move[0]][move[1]].islower():
                pseudo_legal_moves.append(Move(square, to_sq, is_capture = True))
            if side_to_move == 'b' and board[move[0]][move[1]].isuuper():
                pseudo_legal_moves.append(Move(square, to_sq, is_capture = True))
            

    return pseudo_legal_moves
