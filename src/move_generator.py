from .move import Move


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

def generate_pawn_moves(game_state):
    moves = []
    piece = 'p'
    board = game_state.board.board
    side_to_move = game_state.side_to_move
    promotions = ['r', 'n', 'b', 'q']

    if side_to_move == 'w':
        piece = piece.upper()
    
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == piece:
                if side_to_move == 'w':

                    if i == 6:
                        if board[i - 2][j] == '.':
                            moves.append(Move(index_to_square(i, j), index_to_square(i - 2, j)))
                    
                    if board[i - 1][j] == '.':
                        if i > 1: 
                            moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j)))
                        if i == 1:
                            for x in range(len(promotions)):
                                moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j), promotion = promotions[x]))

                    if j >= 1:
                        if board[i - 1][j - 1] != '.':
                            if i > 1:
                                moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j - 1), is_capture = True))
                            if i == 1:
                                for x in range(len(promotions)):
                                    moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j - 1), promotion = promotions[x], is_capture = True))

                        if game_state.en_passant_square == index_to_square(i - 1, j - 1):
                            moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j - 1), is_capture = True, is_en_passant = True))

                    if j <= 6:
                        if board[i - 1][j + 1] != '.':
                            if i > 1:
                                moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j + 1), is_capture = True))
                            if i == 1:
                                for x in range(len(promotions)):
                                    moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j + 1), promotion = promotions[x], is_capture = True))
                        
                        if game_state.en_passant_square == index_to_square(i - 1, j + 1):
                            moves.append(Move(index_to_square(i, j), index_to_square(i - 1, j + 1), is_capture = True, is_en_passant = True))

    return moves