import pytest

from src.game_state import GameState
from src.move_generator.move_generator import generate_pseudo_legal_move as generate_psuedo_legal_moves
from src.move_generator.qrbnk_move_generator import generate_qrb_moves, generate_nk_moves


def assert_moves_contain(moves, expected):
    move_tos = {move.to_sq for move in moves}
    for target in expected:
        assert target in move_tos


@pytest.mark.parametrize(
    "fen, square, expected",
    [
        ("8/8/8/8/4Q3/8/8/8 w - - 0 1", "e4", ["d3", "d4", "d5", "e3", "e5", "f3", "f4", "f5"]),
        ("8/8/8/8/4R3/8/8/8 w - - 0 1", "e4", ["e3", "e5", "d4", "f4"]),
        ("8/8/8/8/4B3/8/8/8 w - - 0 1", "e4", ["d3", "d5", "f3", "f5"]),

        ("8/8/8/8/3Q4/8/8/8 w - - 0 1", "d4", ["c3", "c4", "c5", "d3", "d5", "e3", "e4", "e5"]),
        ("8/8/8/8/3R4/8/8/8 w - - 0 1", "d4", ["d3", "d5", "c4", "e4"]),
        ("8/8/8/8/3B4/8/8/8 w - - 0 1", "d4", ["c3", "c5", "e3", "e5"]),

        ("8/8/8/8/Q7/8/8/8 w - - 0 1", "a4", ["a3", "a5", "b3", "b4", "b5"]),
        ("8/8/8/8/R7/8/8/8 w - - 0 1", "a4", ["a3", "a5", "b4"]),
        ("8/8/8/8/B7/8/8/8 w - - 0 1", "a4", ["b3", "b5"]),

        ("8/8/8/8/7Q/8/8/8 w - - 0 1", "h4", ["g3", "g4", "g5", "h3", "h5"]),
        ("8/8/8/8/7R/8/8/8 w - - 0 1", "h4", ["h3", "h5", "g4"]),
        ("8/8/8/8/7B/8/8/8 w - - 0 1", "h4", ["g3", "g5"]),

        ("4Q3/8/8/8/8/8/8/8 w - - 0 1", "e8", ["e7", "d7", "f7"]),
        ("4R3/8/8/8/8/8/8/8 w - - 0 1", "e8", ["e7", "d8", "f8"]),
        ("4B3/8/8/8/8/8/8/8 w - - 0 1", "e8", ["d7", "f7"]),

        ("8/8/8/8/8/8/8/3Q4 w - - 0 1", "d1", ["d2", "c2", "e2"]),
        ("8/8/8/8/8/8/8/3R4 w - - 0 1", "d1", ["d2", "c1", "e1"]),
        ("8/8/8/8/8/8/8/3B4 w - - 0 1", "d1", ["c2", "e2"]),

        ("8/8/8/8/8/8/1Q6/8 w - - 0 1", "b2", ["a1", "a2", "a3", "b1", "b3", "c1", "c2", "c3"]),
        ("8/8/8/8/8/8/1R6/8 w - - 0 1", "b2", ["b1", "b3", "a2", "c2"]),
    ]
)

def test_qrb_moves_cases(fen, square, expected):
    game_state = GameState(fen)
    assert_moves_contain(generate_qrb_moves(game_state, square), expected)


@pytest.mark.parametrize(
    "fen, square, expected",
    [
        ("8/8/8/8/4N3/8/8/8 w - - 0 1", "e4", ["c3", "d2", "f2", "g3", "g5", "f6", "d6", "c5"]),
        ("8/8/8/8/4K3/8/8/8 w - - 0 1", "e4", ["d3", "d4", "d5", "e3", "e5", "f3", "f4", "f5"]),

        ("8/8/8/8/N7/8/8/8 w - - 0 1", "a4", ["b2", "c3", "c5", "b6"]),
        ("8/8/8/8/K7/8/8/8 w - - 0 1", "a4", ["a3", "a5", "b3", "b4", "b5"]),

        ("8/8/8/8/7N/8/8/8 w - - 0 1", "h4", ["f3", "g2", "g6", "f5"]),
        ("8/8/8/8/7K/8/8/8 w - - 0 1", "h4", ["g3", "g4", "g5", "h3", "h5"]),

        ("4N3/8/8/8/8/8/8/8 w - - 0 1", "e8", ["c7", "d6", "f6", "g7"]),
        ("4K3/8/8/8/8/8/8/8 w - - 0 1", "e8", ["d7", "d8", "e7", "f7", "f8"]),

        ("8/8/8/8/8/8/8/3N4 w - - 0 1", "d1", ["b2", "c3", "f2", "e3"]),
        ("8/8/8/8/8/8/8/3K4 w - - 0 1", "d1", ["c2", "d2", "e2", "c1", "e1"]),

        ("8/8/8/8/8/8/1N6/8 w - - 0 1", "b2", ["a4", "c4", "d1", "d3"]),
        ("8/8/8/8/8/8/1K6/8 w - - 0 1", "b2", ["a1", "a2", "a3", "b1", "b3", "c1", "c2", "c3"]),

        ("8/8/8/8/8/8/6N1/8 w - - 0 1", "g2", ["e1", "e3", "f4", "h4"]),
        ("8/8/8/8/8/8/6K1/8 w - - 0 1", "g2", ["f1", "f2", "f3", "g1", "g3", "h1", "h2", "h3"]),

        ("8/8/2N5/8/8/8/8/8 w - - 0 1", "c6", ["a5", "a7", "b4", "b8", "d4", "d8", "e5", "e7"]),
        ("8/8/2K5/8/8/8/8/8 w - - 0 1", "c6", ["b5", "b6", "b7", "c5", "c7", "d5", "d6", "d7"]),

        ("8/8/5N2/8/8/8/8/8 w - - 0 1", "f6", ["d5", "d7", "e4", "e8", "g4", "g8", "h5", "h7"]),
        ("8/8/5K2/8/8/8/8/8 w - - 0 1", "f6", ["e5", "e6", "e7", "f5", "f7", "g5", "g6", "g7"]),

        ("8/8/8/8/8/8/8/N7 w - - 0 1", "a1", ["b3", "c2"]),
        ("8/8/8/8/8/8/8/K7 w - - 0 1", "a1", ["a2", "b1", "b2"]),
    ],
)

def test_nk_moves_cases(fen, square, expected):
    game_state = GameState(fen)
    assert_moves_contain(generate_nk_moves(game_state, square), expected)