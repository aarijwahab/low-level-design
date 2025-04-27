from game import Game
from player import Player

class Demo:
    def run(self):
        player1 = Player("Player1", "X")
        player2 = Player("Player2", "O")
        game = Game(player1, player2)
        game.play()


if __name__ == "__main__":
    demo = Demo()

    demo.run()