class PawnWhite():
    def __init__(self, position):
        self.alive = True
        self.moved = False
        self.position = position

    def __str__(self):
        return f"PW at {self.position}"

    def available_moves(self, board, black_pieces):
        # REMEMBER TO ONLY CALL AFTER PROMOTE CHECK
        result = set()
        x, y = self.position
        # 1 move ahead
        if board[x][y+1] is None:
            result.add((x, y+1))
            # 2 moves ahead
            if y + 2 < 8:
                if not self.moved and board[x][y+2] is None:
                    result.add((x, y+2))

        # Can eat opfor piece
        if x + 1 < 8:
            if board[x+1][y+1] in black_pieces:
                result.add((x+1, y+1))
        if x - 1 > -1:
            if board[x-1][y+1] in black_pieces:
                result.add((x-1, y+1))

        # en passant
        ...
        return result

    def can_be_promoted(self):
        return self.position[1] == 7
    

class PawnBlack():
    ...


class RookWhite():
    def __init__(self, position, half):
        self.alive = True
        self.moved = False
        self.position = position
        self.half = half

    def __str__(self):
        return f"RW at {self.position}"

    def available_moves(self, board, black_pieces):
        result = set()
        x, y = self.position
        # Check on the right
        r = x + 1
        while r < 7:
            if board[r][y] is not None:
                result.add((r, y))
            elif board[r][y] in black_pieces:
                result.add((r, y))
                break
            else:
                break
            r += 1
        # Check on the left
        l = x - 1
        while l > -1:
            if board[l][y] is not None:
                result.add((l, y))
            elif board[l][y] in black_pieces:
                result.add((l, y))
                break
            else:
                break
            l -= 1
        # Check up
        u = y + 1
        while u < 7:
            if board[x][u] is not None:
                result.add((x, u))
            elif board[x][u] in black_pieces:
                result.add((x, u))
                break
            else:
                break
            u += 1
        # Check down:
        d = y - 1
        while d > -1:
            if board[x][d] is not None:
                result.add((x, d))
            elif board[x][d] in black_pieces:
                result.add((x, d))
                break
            else:
                break
            d -= 1
        # Check castling
        if self.can_castle:
            result.add(self.can_castle)
        return result
    
    def can_castle(self, board, KW_moved, KW_checked=False):
        # https://support.chess.com/article/266-how-do-i-castle
        # Missing rule "Your king can not pass through check"
        if not self.moved and not KW_moved:
            if self.half == "L":
                if any(board[0][y] for y in {1, 2, 3}):
                    return None
                return (0, 3)
            else:
                if any(board[0][y] for y in {5, 6}):
                    return None
                return (0, 5)
        else:
            return None