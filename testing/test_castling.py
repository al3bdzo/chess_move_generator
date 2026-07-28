import pytest

from src.game_state import GameState
from src.move import Move
from src.move_generator.qrbnk_move_generator import handle_castling


@pytest.mark.parametrize(
    "fen,square,expected_moves",
    [
        # White can castle both sides
        (
            "4k3/8/8/8/8/8/8/R3K2R w KQ - 0 1",
            "e1",
            [
                Move("e1", "g1", is_castling=True),
                Move("e1", "c1", is_castling=True),
            ],
        ),

        # White kingside only
        (
            "4k3/8/8/8/8/8/8/R3K2R w K - 0 1",
            "e1",
            [
                Move("e1", "g1", is_castling=True),
            ],
        ),

        # White queenside only
        (
            "4k3/8/8/8/8/8/8/R3K2R w Q - 0 1",
            "e1",
            [
                Move("e1", "c1", is_castling=True),
            ],
        ),

        # Black can castle both sides
        (
            "r3k2r/8/8/8/8/8/8/4K3 b kq - 0 1",
            "e8",
            [
                Move("e8", "g8", is_castling=True),
                Move("e8", "c8", is_castling=True),
            ],
        ),

        # Black kingside only
        (
            "r3k2r/8/8/8/8/8/8/4K3 b k - 0 1",
            "e8",
            [
                Move("e8", "g8", is_castling=True),
            ],
        ),

        # Black queenside only
        (
            "r3k2r/8/8/8/8/8/8/4K3 b q - 0 1",
            "e8",
            [
                Move("e8", "c8", is_castling=True),
            ],
        ),
    ]
)
def test_castling_generated(fen, square, expected_moves):
    state = GameState(fen)

    moves = handle_castling(state, square)

    assert len(moves) == len(expected_moves)

    for move in expected_moves:
        assert move in moves


@pytest.mark.parametrize(
    "fen,square",
    [
        # No castling rights
        (
            "4k3/8/8/8/8/8/8/R3K2R w - - 0 1",
            "e1",
        ),

        # blocked
        (
            "4k3/8/8/8/8/8/8/RN2KN1R w KQ - 0 1",
            "e1",
        ),

        # rooks missing
        (
            "4k3/8/8/8/8/8/8/4K3 w KQ - 0 1",
            "e1",
        ),

        # White king in check
        (
            "4k3/8/8/8/8/8/4r3/R3K2R w KQ - 0 1",
            "e1",
        ),

        # attacked
        (
            "4k3/8/8/8/8/8/2r2r2/R3K2R w KQ - 0 1",
            "e1",
        ),

        # attacked
        (
            "4k3/8/8/8/8/2r3r1/8/R3K2R w KQ - 0 1",
            "e1",
        ),

        # Black king in check
        (
            "r3k2r/4R3/8/8/8/8/8/4K3 b kq - 0 1",
            "e8",
        ),


        # blocked
        (
            "rn2k1nr/8/8/8/8/8/8/4K3 b kq - 0 1",
            "e8",
        ),

        (
            "4k3/8/8/8/8/8/8/R3K2R w KQ - 0 1",
            "d1",
        ),

        (
            "r3k2r/8/8/8/8/8/8/4K3 b kq - 0 1",
            "d8",
        ),
    ]
)
def test_castling_not_generated(fen, square):
    state = GameState(fen)

    moves = handle_castling(state, square)

    assert moves == []