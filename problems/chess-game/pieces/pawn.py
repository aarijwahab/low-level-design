from piece import Piece

class Pawn(Piece):
    
    def can_move(self, board, dest_row, dest_col):
        row_diff = dest_row - self.row
        col_diff = abs(dest_col - self.col)

        if self.colour == "WHITE":
            forward = (row_diff == 1 and col_diff == 0)
            startingMove = (self.row == 1 and self.row_diff == 2 and col_diff == 0)
            takePiece = (row_diff == 1 and col_diff == 1 and board.get_piece(dest_row, dest_col) is not None)
        else:
            forward = (row_diff == -1 and col_diff == 0)
            startingMove = (self.row == 6 and self.row_diff == -2 and col_diff == 0)
            takePiece = (row_diff == -1 and col_diff == 1 and board.get_piece(dest_row, dest_col) is not None)
        return forward or startingMove or takePiece