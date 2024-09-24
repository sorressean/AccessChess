from .abstract_broker import AbstractBroker


class Broker(AbstractBroker):
    def __init__(self):
        self.game = None
        self.board = None

    def set_board(self, board):
        self.board = board

    def set_game(self, game):
        self.game = game

    def on_new_game(self):
        if self.game is not None:
            self.game.on_new_game()
        if self.board is not None:
            self.board.on_new_game()


broker = Broker()
