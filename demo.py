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
class Chess:
    white_pieces = (RW, NW, BW, QW, KW, BW, NW, RW, PW)
    black_pieces = (RB, NB, BB, QB, KB, BB, NB, RB, PB)
    def __init__(self) -> None:
        self.board = self.get_initial_board()
        self.move_count = 0
    
    # actions
    def player(self):
        if self.move_count % 2 == 0:
            return WHITE
        else:
            return BLACK
        
    @classmethod
    def get_active_pieces(cls, player, board):
        """
        takes player and returns all the active pieces for that player in 
        '(piece-name, row, column)' format
        """
        active_pieces_lst = []
        if player == BLACK:
            for row_num, row in enumerate(board):
                for cell_num, cell in enumerate(row):
                    if cell in cls.black_pieces:
                        active_pieces_lst.append((cell, row_num, cell_num))
        elif player == WHITE:
            for row_num, row in enumerate(board):
                for cell_num, cell in enumerate(row):
                    if cell in cls.white_pieces:
                        active_pieces_lst.append((cell, row_num, cell_num))
        else:
            raise ValueError("only black or white pieces")
        
        return active_pieces_lst
    
    def get_actions(self, active_pieces_lst, board):
        action_list = []
        for piece in active_pieces_lst:
            if piece[0] == PW or piece[0] == PB:
                action_list.append(self.pawn_actions(piece=piece, board=board))
            elif piece[0] == KW or piece[0] == KB:
                action_list.append(self.king_actions(piece=piece, board=board))
            elif piece[0] == QW or piece[0] == QB:
                action_list.append(self.queen_actions(piece=piece, board=board))
            elif piece[0] == RW or piece[0] == RB:
                action_list.append(self.rook_actions(piece=piece, board=board))
            elif piece[0] == BW or piece[0] == BB:
                action_list.append(self.bishop_actions(piece=piece, board=board))
            elif piece[0] == NW or piece[0] == NB:
                action_list.append(self.knight_actions(piece, board))

        return action_list


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
    def get_initial_board(cls):
        board = []
        board.append(cls.create_back_rank(BLACK))
        board.append(cls.create_pawn_row(BLACK))
        for i in range(6):
            board.append(cls.create_empty_row())
        board.append(cls.create_back_rank(WHITE))
        board.append(cls.create_pawn_row(WHITE))
        return board

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
    
    def print_board(self):
        table = tabulate(self.board, tablefmt="grid")
        print(table)

action_dict = {
    "player" : WHITE,
    "piece" : PW,
    "source" : (1, 1),
    "target" : (2, 1)
    # or -> (player, piece, source, target)
}

# piece
chess = Chess()
chess.print_board()
""" 
King: K
Queen: Q
Rook: R
Bishop: B
Knight: N (Note: N is used instead of K to avoid confusion with the King's abbreviation)
Pawn: P (Pawns are usually represented by the absence of an abbreviation)
blank: None

I need a way to see the all the active pieces on board
    so that I can see their moves later
    the information I need - name, position (name, position)

I need action validator function

"""