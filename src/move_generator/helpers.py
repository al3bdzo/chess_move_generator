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

def is_on_the_board(i, j):
    if i >= 0 and i <= 7 and j >= 0 and j <= 7:
        return True
    return False

def get_piece(board, square):
    i, j = square_to_index(square)
    return board[i][j]


def can_capture(moving_piece, captured_piece):
    if moving_piece.isupper() and captured_piece.islower():
        return True
    if moving_piece.islower() and captured_piece.isupper():
        return True
    return False

def is_rank(i, rank_index):
    if i == rank_index:
        return True
    return False

def is_double_pawn_push(board, i, j, di, dj):
    if abs(i - di) != 2:
        return False
    if j != dj:
        return False
    if get_piece(board, index_to_square(di, dj)) != '.':
        return False
    middle_rank = (i + di) // 2

    if get_piece(board, index_to_square(middle_rank, dj)) != '.':
        return False
    return True