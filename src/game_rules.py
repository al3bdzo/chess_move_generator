from .move_generator.helpers import square_to_index, index_to_square, get_piece, is_on_the_board
from .constants import WHITE_PAWN_ATTACKS, BLACK_PAWN_ATTACKS, KNIGHT_OFFSET, KING_OFFSET, BISHOP_DIRECTIONS, ROOK_DIRECTIONS, QUEEN_DIRECTIONS

def is_attacked_by_kpn(board, square, offset, attacker):
    rank, file = square_to_index(square)
    
    for di, dj in offset:
        i = rank + di
        j = file + dj
        if is_on_the_board(i, j):
            if get_piece(board, index_to_square(i, j)) == attacker:
                return True
    return False

def is_attacked_by_rbq(board, square, directions, attackers):
    rank, file = square_to_index(square)
    for di, dj in directions:
        i = rank
        j = file
        while True:
            i = i + di
            j = j + dj
            if is_on_the_board(i, j):
                attacking_piece = get_piece(board, index_to_square(i, j))
                if attacking_piece == '.':
                    continue
                elif attacking_piece in attackers:
                    return True
                else:
                    break
            else: 
                break
    return False

def is_square_attacked(game_state, square, attacker_side):

    if attacker_side not in {"w", "b"}:
        raise ValueError(f"{attacker_side} is not a side to play in chess")

    board = game_state.board.board

    pawn = 'p'
    knight = 'n'
    king = 'k'
    bishop = 'b'
    rook = 'r'
    queen = 'q'

    # the attacks are swapped because we search for an attacker in the opposite side
    pawn_attacks = WHITE_PAWN_ATTACKS

    if attacker_side == 'w':
        pawn_attacks = BLACK_PAWN_ATTACKS
        
        pawn = 'P'
        knight = 'N'
        king = 'K'
        bishop = 'B'
        rook = 'R'
        queen = 'Q'
    
    pawn_attack = is_attacked_by_kpn(board, square, pawn_attacks, pawn)
    knight_attack = is_attacked_by_kpn(board, square, KNIGHT_OFFSET, knight)
    king_attack = is_attacked_by_kpn(board, square, KING_OFFSET, king)
    bishop_attack = is_attacked_by_rbq(board, square, BISHOP_DIRECTIONS, {bishop, queen})
    rook_attack = is_attacked_by_rbq(board, square, ROOK_DIRECTIONS, {rook, queen})

    return pawn_attack or knight_attack or king_attack or bishop_attack or rook_attack 