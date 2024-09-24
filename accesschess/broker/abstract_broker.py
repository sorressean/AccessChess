from abc import ABC, abstractmethod


class AbstractBroker(ABC):
    @abstractmethod
    def set_board(self, board):
        """
        Sets the board for the broker.
        This will proxy board operations to the board from the UI.
        """

    @abstractmethod
    def set_game(self, game):
        """
        Sets the game for the broker.
        Proxies game operations from the UI to the game.
        """

    @abstractmethod
    def on_new_game(self):
        """
        Notifies the game object and the panel of a new game beginning.
        Order of operations is to notify game first, then panel.
        """
