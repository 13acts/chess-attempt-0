from tabulate import tabulate
from copy import deepcopy

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
        
    def print_board(self):
        table = tabulate(self.board, tablefmt="grid")
        print(table)

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
            row.append(E)
        return row
    
    # get pieces that are on chess board along with their location of the particular player
    @classmethod
    def get_active_pieces(cls, player, chessboard):
        """
        takes player and returns all the active pieces for that player in 
        '(piece-name, row, column)' format
        """
        active_pieces_lst = []
        board = chessboard.board
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
    
    @classmethod
    def result(cls, chessboard, action, move_num):
        """
        returns resulting board 

        action variable should contain contain tuple - (player, piece, source, target, castling, side)
        source and target will be tuples themselves 

        will assume that actions are correct
        """
        # validating input type
        if not isinstance(board, ChessBoard) and not isinstance(action, tuple):
            raise TypeError
        if len(tuple) != 4 and len(tuple) != 6:
            raise ValueError
        
        # r
        player = action[0]
        piece = action[1]
        source = action[2]
        target = action[3]
        board = deepcopy(chessboard.board)

        # if castling
        if len(action) == 5:
            if player == BLACK and chessboard.black_castled:
                ...
                # TODO return board with castling
            elif player == WHITE and chessboard.white_castled:
                ...
                # TODO return board with castling

        # pawn promotes to queen at last square
        if board[source[0]][source[1]] == PW and source[0] == 1:
            board[source[0]][source[1]] =  E
            board[target[0]][target[1]] = QW

        elif board[source[0]][source[1]] == PB and source[0] == 6:
            board[source[0]][source[1]] =  E
            board[target[0]][target[1]] = QB
        else:
            board[source[0]][source[1]] =  E
            board[target[0]][target[1]] = piece

        return ChessBoard(board=board, move_num=move_num)
        # 

            

    
"""
first I define my result function then go backwards
"""