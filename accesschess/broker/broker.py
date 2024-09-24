from .abstract_broker import AbstractBroker


class Broker(AbstractBroker):
    def __init__(self):
        self.game = None
        self.board = None

    def set_board(self, board):
        self.board = board

    def set_game(self, game):
        self.game = game

    def get_grid(self):
        if self.game is not None:
            return self.game.get_grid_mapping()
        else:
            return [[" " for _ in range(8)] for _ in range(8)]

    def on_new_game(self):
        if self.game is not None:
            self.game.on_new_game()
        if self.board is not None:
            self.board.on_new_game()

    def on_left_edge(self):
        """
        Typically we would probably expect the UI to play this sound.
        For easier handling however we should leave sound playing to
        the game and play from there.
        Therefore only trigger on the game object by default.
        """
        self.game.on_left_edge()

    def on_top_edge(self):
        """
        Typically we would probably expect the UI to play this sound.
        For easier handling however we should leave sound playing to
        the game and play from there.
        Therefore only trigger on the game object by default.
        """
        self.game.on_top_edge()
