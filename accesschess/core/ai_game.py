from .game import Game
import chess
import chess.engine

class AIGame(Game):
    stockfish_path="engines/stockfish-fast.exe"
    def __init__(self):
        super().__init__()

    def initialize_game(self):
        super().initialize_game()
        self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path)

    def get_options(self):
        if self.engine is None:
            return {}
        return self.engine.options
    