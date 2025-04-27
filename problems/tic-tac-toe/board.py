class Board:
    def __init__(self):
        self.grid = [["-" for _ in range(3)] for _ in range(3)]
        self.moves_played = 0

    def __str__(self):
        string_rep = ""
        for row in self.grid:
            string_rep += " ".join(row) + "\n"
        return string_rep
    
    def makeMove(self, row, col, symbol):
        row_in_bounds = 0 <= row < 3
        col_in_bounds = 0 <= col < 3
        if not row_in_bounds or not col_in_bounds or self.grid[row][col] != "-":
            raise ValueError("Invalid Move!")
        self.grid[row][col] = symbol
        self.moves_played += 1
    
    def checkWinner(self):
        # Check rows
        for row in self.grid:
            if row[0] != "-" and (row[0] == row[1] == row[2]):
                return row[0]  # Return the symbol, not player object

        # Check columns
        for col in range(3):
            if self.grid[0][col] != "-" and (self.grid[0][col] == self.grid[1][col] == self.grid[2][col]):
                return self.grid[0][col]

        # Check diagonals
        if self.grid[0][0] != "-" and (self.grid[0][0] == self.grid[1][1] == self.grid[2][2]):
            return self.grid[0][0]

        if self.grid[0][2] != "-" and (self.grid[0][2] == self.grid[1][1] == self.grid[2][0]):
            return self.grid[0][2]

        # No winner
        return None


    def checkTie(self):
        return self.moves_played == 9