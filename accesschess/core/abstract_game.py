from abc import ABC, abstractmethod


class AbstractGame(ABC):
    @abstractmethod
    def initialize_game(self):
        """
        Initialize the game board and other game-related properties.
        """

    @abstractmethod
    def get_grid_mapping(self):
        """
        Get the current mapping of the chessboard with all pieces in their respective positions.

        Returns:
            list of lists: A 2D array where each entry represents a square on the board.
        """

    @abstractmethod
    def on_new_game(self):
        pass
