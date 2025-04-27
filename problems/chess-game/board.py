from pieces.piece import Piece
from pieces.rook import Rook
from pieces.pawn import Pawn
from pieces.king import King
from pieces.queen import Queen
from pieces.bishop import Bishop
from pieces.knight import Knight
from colour import Colour


class ChessBoard():
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self._initialize_board()


    def _initialize_board(self):
        # Initialize white pieces
        self.board[0][0] = Rook(Colour.WHITE, 0, 0)
        self.board[0][1] = Knight(Colour.WHITE, 0, 1)
        self.board[0][2] = Bishop(Colour.WHITE, 0, 2)
        self.board[0][3] = Queen(Colour.WHITE, 0, 3)
        self.board[0][4] = King(Colour.WHITE, 0, 4)
        self.board[0][5] = Bishop(Colour.WHITE, 0, 5)
        self.board[0][6] = Knight(Colour.WHITE, 0, 6)
        self.board[0][7] = Rook(Colour.WHITE, 0, 7)
        for i in range(8): # Pawns
            self.board[1][i] = Pawn(Colour.WHITE, 1, i)

        # Initialize black pieces
        self.board[7][0] = Rook(Colour.BLACK, 7, 0)
        self.board[7][1] = Knight(Colour.BLACK, 7, 1)
        self.board[7][2] = Bishop(Colour.BLACK, 7, 2)
        self.board[7][3] = Queen(Colour.BLACK, 7, 3)
        self.board[7][4] = King(Colour.BLACK, 7, 4)
        self.board[7][5] = Bishop(Colour.BLACK, 7, 5)
        self.board[7][6] = Knight(Colour.BLACK, 7, 6)
        self.board[7][7] = Rook(Colour.BLACK, 7, 7)
        for i in range(8):
            self.board[6][i] = Pawn(Colour.BLACK, 6, i)

    def get_piece(self, row, col):
        return self.board[row][col]

    def is_valid_move(self, piece, dest_row, dest_col):
        if piece is None or dest_row < 0 or dest_row > 7 or dest_col < 0 or dest_col > 7:
            return False
        dest_piece = self.board[dest_row][dest_col]
        return (dest_piece is None or dest_piece.colour != piece.colour) and \
               piece.can_move(self, dest_row, dest_col)


    def is_checkmate(self, color):
        # TODO: Implement checkmate logic
        return False

    def is_stalemate(self, color):
        # TODO: Implement stalemate logic
        return False
