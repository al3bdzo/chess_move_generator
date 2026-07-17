from ..move import Move
from ..constants import BISHOP_DIRECTIONS
from .helpers import square_to_index, is_on_the_board, index_to_square, get_piece

def generate_bishop_moves(game_state, square):
    board = game_state.board.board
    side_to_move = game_state.side_to_move

    moves = []

    i, j = square_to_index(square)

    for direction in BISHOP_DIRECTIONS:
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
    