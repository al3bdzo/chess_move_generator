from dataclasses import dataclass 
from typing import Optional

@dataclass
class Move:
    from_sq: str
    to_sq: str
    promotion: Optional[str] = None
    is_capture: bool = False
    captured_piece: Optional[str] = None
    is_castling: bool = False
    is_en_passant: bool = False
    is_double_pawn_push: bool = False