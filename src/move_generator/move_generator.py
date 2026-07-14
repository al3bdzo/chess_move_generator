from ..move import Move

def index_to_square(rank_index, file_index):
    square = ''
    square += chr(file_index + 97)
    ranks = ['8', '7', '6', '5', '4', '3', '2', '1']
    square += ranks[rank_index]
    return square

def square_to_index(square):
    file_index = ord(square[0]) - 97
    rank_indexes = [7, 6, 5, 4, 3, 2, 1, 0]
    rank_index = rank_indexes[int(square[1]) - 1]
    return rank_index, file_index


def generate_pseudo_legal_move(game_state):
    from .pawn_move_generator import generate_white_pawn_moves

    board = game_state.board.board
    side_to_move = game_state.side_to_move
    en_passant_square = game_state.en_passant_square
    moves = []

    for i in range(len(board)):
        for j in range(len(board[i])):
            if side_to_move == 'w':
                piece = board[i][j]
                square = index_to_square(i, j)
                match piece:
                    case '.':
                        continue
                    case 'P':
                        moves.extend(generate_white_pawn_moves(game_state, square))
            elif side_to_move == 'b':
                pass

    return moves