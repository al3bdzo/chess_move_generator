from ..move import Move
from .helpers import index_to_square, square_to_index

def generate_pawn_moves(game_state, square):
    if game_state.side_to_move == 'w':
        return generate_white_pawn_moves(game_state, square)

    return generate_black_pawn_moves(game_state, square)

def generate_white_pawn_moves(game_state, square):
    board = game_state.board.board
    en_passant_square = game_state.en_passant_square
    moves = []
    promotions = ['R', 'N', 'B', 'Q']

    i, j = square_to_index(square)

    if i < 7 and i > 0:
        if i == 6:
            if board[i - 2][j] == '.' and board[i - 1][j] == '.':
                moves.append(Move(square, index_to_square(i - 2, j), is_double_pawn_push = True))
        
        if board[i - 1][j] == '.':
            if i > 1: 
                moves.append(Move(square, index_to_square(i - 1, j)))
            if i == 1:
                for x in range(len(promotions)):
                    moves.append(Move(square, index_to_square(i - 1, j), promotion = promotions[x]))

        if j >= 1:
            if board[i - 1][j - 1] != '.' and board[i - 1][j - 1].islower():
                if i > 1:
                    moves.append(Move(square, index_to_square(i - 1, j - 1), is_capture = True))
                if i == 1:
                    for x in range(len(promotions)):
                        moves.append(Move(square, index_to_square(i - 1, j - 1), promotion = promotions[x], is_capture = True))

            if en_passant_square == index_to_square(i - 1, j - 1):
                moves.append(Move(square, index_to_square(i - 1, j - 1), is_capture = True, is_en_passant = True))

        if j <= 6:
            if board[i - 1][j + 1] != '.' and board[i - 1][j + 1].islower():
                if i > 1:
                    moves.append(Move(square, index_to_square(i - 1, j + 1), is_capture = True))
                if i == 1:
                    for x in range(len(promotions)):
                        moves.append(Move(square, index_to_square(i - 1, j + 1), promotion = promotions[x], is_capture = True))
            
            if en_passant_square == index_to_square(i - 1, j + 1):
                moves.append(Move(square, index_to_square(i - 1, j + 1), is_capture = True, is_en_passant = True))

    return moves


def generate_black_pawn_moves(game_state, square):
    board = game_state.board.board
    en_passant_square = game_state.en_passant_square
    moves = []
    promotions = ['r', 'n', 'b', 'q']

    i, j = square_to_index(square)

    if i > 0 and i < 7:
        if i == 1:
            if board[i + 2][j] == '.' and board[i + 1][j] == '.':
                moves.append(Move(square, index_to_square(i + 2, j), is_double_pawn_push = True))
        
        if board[i + 1][j] == '.':
            if i < 6: 
                moves.append(Move(square, index_to_square(i + 1, j)))
            if i == 6:
                for x in range(len(promotions)):
                    moves.append(Move(square, index_to_square(i + 1, j), promotion = promotions[x]))

        if j >= 1:
            if board[i + 1][j - 1] != '.' and board[i + 1][j - 1].isupper():
                if i < 6:
                    moves.append(Move(square, index_to_square(i + 1, j - 1), is_capture = True))
                if i == 6:
                    for x in range(len(promotions)):
                        moves.append(Move(square, index_to_square(i + 1, j - 1), promotion = promotions[x], is_capture = True))

            if en_passant_square == index_to_square(i + 1, j - 1):
                moves.append(Move(square, index_to_square(i + 1, j - 1), is_capture = True, is_en_passant = True))

        if j <= 6:
            if board[i + 1][j + 1] != '.' and board[i + 1][j + 1].isupper():
                if i < 6:
                    moves.append(Move(square, index_to_square(i + 1, j + 1), is_capture = True))
                if i == 6:
                    for x in range(len(promotions)):
                        moves.append(Move(square, index_to_square(i + 1, j + 1), promotion = promotions[x], is_capture = True))
            
            if en_passant_square == index_to_square(i + 1, j + 1):
                moves.append(Move(square, index_to_square(i + 1, j + 1), is_capture = True, is_en_passant = True))

    return moves

