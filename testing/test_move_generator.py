from src.game_state import GameState
from src.move_generator.move_generator import generate_pseudo_legal_move
from src.move import Move
from src.move_generator.bishop_move_generator import generate_bishop_moves
from src.move_generator.queen_move_generator import generate_queen_moves
from src.move_generator.rook_move_generator import generate_rook_moves

import pytest

@pytest.mark.parametrize("game_state, moves", [
    (
        GameState("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w - - 0 1"),
        [
            Move("a2", "a3"),
            Move("a2", "a4", is_double_pawn_push=True),

            Move("b2", "b3"),
            Move("b2", "b4", is_double_pawn_push=True),

            Move("c2", "c3"),
            Move("c2", "c4", is_double_pawn_push=True),

            Move("d2", "d3"),
            Move("d2", "d4", is_double_pawn_push=True),

            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),

            Move("f2", "f3"),
            Move("f2", "f4", is_double_pawn_push=True),

            Move("g2", "g3"),
            Move("g2", "g4", is_double_pawn_push=True),

            Move("h2", "h3"),
            Move("h2", "h4", is_double_pawn_push=True),

            Move("b1", "a3"),
            Move("b1", "c3"),

            Move("g1", "f3"),
            Move("g1", "h3"),
        ]
    ),

    (
        GameState("8/8/8/8/8/3P1P2/2PNP3/8 w - - 0 1"),
        [
            Move("d3", "d4"),

            Move("f3", "f4"),

            Move("c2", "c3"),
            Move("c2", "c4", is_double_pawn_push=True),

            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),

            Move("d2", "b1"),
            Move("d2", "b3"),
            Move("d2", "c4"),
            Move("d2", "e4"),
            Move("d2", "f1"),
        ]
    ),

    (
        GameState("8/8/8/3p1p2/8/4N3/8/8 w - - 0 1"),
        [
            Move("e3", "c2"),
            Move("e3", "c4"),
            Move("e3", "d1"),
            Move("e3", "d5", is_capture=True),
            Move("e3", "f1"),
            Move("e3", "f5", is_capture=True),
            Move("e3", "g2"),
            Move("e3", "g4"),
        ]
    ),

    (
        GameState("8/8/8/3p4/4P3/2N5/8/8 w - - 0 1"),
        [
            Move("e4", "e5"),
            Move("e4", "d5", is_capture=True),

            Move("c3", "a2"),
            Move("c3", "a4"),
            Move("c3", "b1"),
            Move("c3", "b5"),
            Move("c3", "d1"),
            Move("c3", "d5", is_capture=True),
            Move("c3", "e2"),
        ]
    ),

    (
        GameState("8/8/8/8/8/8/8/N7 w - - 0 1"),
        [
            Move("a1", "b3"),
            Move("a1", "c2"),
        ]
    ),

    (
        GameState("8/8/8/8/8/8/N7/8 w - - 0 1"),
        [
            Move("a2", "b4"),
            Move("a2", "c3"),
            Move("a2", "c1"),
        ]
    ),

    (
        GameState("8/4P3/8/8/8/4N3/8/8 w - - 0 1"),
        [
            Move("e7", "e8", promotion="Q"),
            Move("e7", "e8", promotion="R"),
            Move("e7", "e8", promotion="B"),
            Move("e7", "e8", promotion="N"),

            Move("e3", "c2"),
            Move("e3", "c4"),
            Move("e3", "d1"),
            Move("e3", "d5"),
            Move("e3", "f1"),
            Move("e3", "f5"),
            Move("e3", "g2"),
            Move("e3", "g4"),
        ]
    ),
])