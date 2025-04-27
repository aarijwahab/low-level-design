from board import Board
from player import Player
class Game:
    def __init__(self, player1: Player, player2: Player):
        self.board = Board()
        self.player1: Player = player1
        self.player2: Player = player2


    def play(self):
        current_player = self.player1

        while not self.board.checkWinner() or not self.board.checkTie():
            print(self.board)
            move = input(f"{current_player.getName()}, make your move: (row,col)")
            try:
                row, col = move.split(',')
                row, col = int(row), int(col)
                self.board.makeMove(row, col, current_player.getSymbol())
                if self.board.checkWinner():
                    print(f"{current_player.getName()} wins!")
                    return
                elif self.board.checkTie():
                    print("It's a tie!")
                    return
                current_player = self.player2 if current_player == self.player1 else self.player1
            except Exception:
                print("Invalid move")