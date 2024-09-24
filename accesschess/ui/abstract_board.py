from abc import ABC, abstractmethod


class AbstractBoard(ABC):
    @abstractmethod
    def create_ui(self):
        """
        Create the user interface for the chessboard, including captured pieces, buttons for squares, etc.
        """

    @abstractmethod
    def on_new_game(self):
        pass
