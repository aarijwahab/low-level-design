from abc import ABC, abstractmethod
class Piece(ABC):
    def __init__(self, colour, row, col):
        self.colour = colour
        self.row = row
        self.col = col

    @abstractmethod
    def can_move(self, board, dest_row, dest_col):
        """
        A method that says whether this is a valid move or not
        E.g. A pawn can only move forward 1 or diagonal to take
        """
        pass