class Board:
    def __init__(self, fen=None):
        self.fen = fen
        self.board = [
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r'],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.', '.', '.'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        ]
        if self.fen:
            self.build_from_fen()

    # just build the board from the FEN not the whole geme state, that's handeled eleswhere
    def build_from_fen(self):
        if self.fen == None:
            return
        
        fen_list = self.fen.split('/')
        if len(fen_list) != 8:
            raise ValueError(f"Expected 8 ranks, found = {len(fen_list)}")

        i = 0
        for rank in fen_list:
            j = 0
            for c in rank:
                if c.isdigit():
                    for z in range(0, int(c)):
                        if j >= 8:
                            raise ValueError(f"Invalid FEN: rank {i+1} has too many squares")
                        self.board[i][j] = '.'
                        j += 1
                else:
                    if j >= 8:
                        raise ValueError(f"Invalid FEN: rank {i+1} has too many squares")
                    self.board[i][j] = c
                    j += 1
            if j != 8:
                raise ValueError(f"Invalid FEN: rank {i+1} has too many squares")
            i += 1 
    
    def __repr__(self):
        representation = ""
        for i in range(0, len(self.board)):
            representation += f"{self.board[i]}\n"
        return representation
    