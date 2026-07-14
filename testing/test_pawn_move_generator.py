from src.game_state import GameState
from src.move_generator.pawn_move_generator import generate_white_pawn_moves
from src.move import Move

import pytest

def sort_moves(moves): 
    return sorted(moves, key=lambda x: (x.from_sq, x.to_sq, x.promotion or ""))

@pytest.mark.parametrize("game_state, square, moves", [
    (
        GameState("8/8/8/8/8/8/4P3/8 w - - 0 1"),
        "e2",
        [
            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),
        ],
    ),
    (
        GameState("8/8/8/8/8/4p3/4P3/8 w - - 0 1"),
        "e2",
        [],
    ),
    (
        GameState("8/8/8/8/8/3p4/4P3/8 w - - 0 1"),
        "e2",
        [
            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),
            Move("e2", "d3", is_capture=True),
        ],
    ),
    (
        GameState("8/8/8/8/8/5p2/4P3/8 w - - 0 1"),
        "e2",
        [
            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),
            Move("e2", "f3", is_capture=True),
        ],
    ),
    (
        GameState("8/8/8/8/8/3p1p2/4P3/8 w - - 0 1"),
        "e2",
        [
            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),
            Move("e2", "d3", is_capture=True),
            Move("e2", "f3", is_capture=True),
        ],
    ),
    (
        GameState("8/8/8/8/8/4P3/8/8 w - - 0 1"),
        "e3",
        [
            Move("e3", "e4"),
        ],
    ),
    (
        GameState("8/8/8/8/8/1p6/P7/8 w - - 0 1"),
        "a2",
        [
            Move("a2", "a3"),
            Move("a2", "a4", is_double_pawn_push=True),
            Move("a2", "b3", is_capture=True),
        ],
    ),
    (
        GameState("8/8/8/8/8/6p1/7P/8 w - - 0 1"),
        "h2",
        [
            Move("h2", "h3"),
            Move("h2", "h4", is_double_pawn_push=True),
            Move("h2", "g3", is_capture=True),
        ],
    ),
    (
        GameState("8/4P3/8/8/8/8/8/8 w - - 0 1"),
        "e7",
        [
            Move("e7", "e8", promotion="Q"),
            Move("e7", "e8", promotion="R"),
            Move("e7", "e8", promotion="B"),
            Move("e7", "e8", promotion="N"),
        ],
    ),
    (
        GameState("5r2/4P3/8/8/8/8/8/8 w - - 0 1"),
        "e7",
        [
            Move("e7", "e8", promotion="Q"),
            Move("e7", "e8", promotion="R"),
            Move("e7", "e8", promotion="B"),
            Move("e7", "e8", promotion="N"),
            Move("e7", "f8", promotion="Q", is_capture=True),
            Move("e7", "f8", promotion="R", is_capture=True),
            Move("e7", "f8", promotion="B", is_capture=True),
            Move("e7", "f8", promotion="N", is_capture=True),
        ],
    ),
    (
        GameState("8/8/8/8/4p3/8/4P3/8 w - - 0 1"),
        "e2",
        [
            Move("e2", "e3"),
        ],
    ),
    (
        GameState("8/8/8/8/3P4/8/4P3/8 w - - 0 1"),
        "e2",
        [
            Move("e2", "e3"),
            Move("e2", "e4", is_double_pawn_push=True),
        ],
    ),
    (
        GameState("3r1r2/4P3/8/8/8/8/8/8 w - - 0 1"),
        "e7",
        [
            Move("e7", "e8", promotion="Q"),
            Move("e7", "e8", promotion="R"),
            Move("e7", "e8", promotion="B"),
            Move("e7", "e8", promotion="N"),

            Move("e7", "d8", promotion="Q", is_capture=True),
            Move("e7", "d8", promotion="R", is_capture=True),
            Move("e7", "d8", promotion="B", is_capture=True),
            Move("e7", "d8", promotion="N", is_capture=True),

            Move("e7", "f8", promotion="Q", is_capture=True),
            Move("e7", "f8", promotion="R", is_capture=True),
            Move("e7", "f8", promotion="B", is_capture=True),
            Move("e7", "f8", promotion="N", is_capture=True),
        ],
    ),
    (
        GameState("8/8/8/3pP3/8/8/8/8 w - d6 0 1"),
        "e5",
        [
            Move("e5", "e6"),
            Move("e5", "d6", is_capture=True, is_en_passant=True),
        ],
    ),
    (
        GameState("8/8/8/4Pp2/8/8/8/8 w - f6 0 1"),
        "e5",
        [
            Move("e5", "e6"),
            Move("e5", "f6", is_capture=True, is_en_passant=True),
        ],
    ),
    (
        GameState("8/8/8/8/8/8/8/4P3 w - - 0 1"),
        "e1",
        [],
    ),
    (
        GameState("4P3/8/8/8/8/8/8/8 w - - 0 1"),
        "e8",
        [],
    ),
])

def test_white_pawn_move_generate(game_state, square, moves):
    assert sort_moves(generate_white_pawn_moves(game_state, square)) == sort_moves(moves)
