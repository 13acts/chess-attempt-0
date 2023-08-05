from tabulate import tabulate

# white pieces
PW = " ♙ " # represents white pawn 
KW = " ♔ " # represents white king
QW = " ♕ " # represents white queen 
RW = " ♖ " # represents white rook 
BW = " ♗ " # represents white bishop 
NW = " ♘ " # represents white knight

# black pieces
PB = " ♟︎ " # represents black pawn
KB = " ♚ " # represents black king
QB = " ♛ " # represents black queen 
RB = " ♜ " # represents black rook 
BB = " ♝ " # represents black bishop 
NB = " ♞ " # represents black knight
BLACK = "BLACK" 
WHITE = "WHITE"
E = None # represents empty 

class ChessBoard():
    def __init__(self, board, move_num, black_castled=False, white_castled=False) -> None:
        self.board = board
        self.move_num = move_num
        self.black_castled = black_castled
        self.white_castled = white_castled
        pass

    # returns whose turn it is
    def player(self):
        if self.move_num % 2 == 0:
            return WHITE
        else:
            return BLACK

class Chess:
    white_pieces = (RW, NW, BW, QW, KW, BW, NW, RW, PW)
    black_pieces = (RB, NB, BB, QB, KB, BB, NB, RB, PB)

    def __init__(self) -> None:
        self.board = self.get_initial_board()
        self.move_count = 0

    @classmethod
    def get_initial_board(cls):
        board = []
        board.append(cls.create_back_rank(BLACK))
        board.append(cls.create_pawn_row(BLACK))
        for i in range(6):
            board.append(cls.create_empty_row())
        board.append(cls.create_back_rank(WHITE))
        board.append(cls.create_pawn_row(WHITE))
        return ChessBoard(board=board, move_num=0)
    
    # setting up the chess board
    @classmethod
    def create_back_rank(cls, player):
        if player == WHITE:
            return [RW, NW, BW, QW, KW, BW, NW, RW]
        if player == BLACK:
            return [RB, NB, BB, QB, KB, BB, NB, RB]
        else:
            raise ValueError

        
    @classmethod
    def create_pawn_row(cls, player):
        row = []
        if player == BLACK:
            for i in range(8):
                row.append(PB)
        elif player == WHITE:
            for i in range(8):
                row.append(PW)
        else:
            raise ValueError
        return row
    
    @classmethod
    def create_empty_row(cls):
        row = []
        for i in range(8):
            row.append(None)
        return row
    
