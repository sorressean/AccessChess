import chess
import chess.engine

from accesschess.core.options import Option, OptionType

from .game import Game


class AIGame(Game):
    stockfish_path = "engines/stockfish-fast.exe"

    def __init__(self):
        super().__init__()
        self.engine = None  # Initialize engine variable in constructor
        self.initialize_game()

    def initialize_game(self):
        super().initialize_game()
        self.engine = chess.engine.SimpleEngine.popen_uci(self.stockfish_path)

    def translate_engine_option(self, engine_option):
        """
        Translates the engine options returned into our options interface.
        """
        option_type = engine_option.type
        default_value = engine_option.default

        if option_type == "string":
            if default_value == "<empty>":
                default_value = ""
            metadata = {"default": default_value}
            return Option(OptionType.String, engine_option.name, default_value, metadata)

        elif option_type == "check":
            metadata = {"default": default_value}
            return Option(OptionType.Boolean, engine_option.name, default_value, metadata)

        elif option_type == "spin":
            metadata = {
                "default": engine_option.__dict__.get("default", 0),
                "min": engine_option.__dict__.get("min", 0),
                "max": engine_option.__dict__.get("max", 0),
            }
            return Option(OptionType.Number, engine_option.name, default_value, metadata)

        else:
            print(f"Error converting option: {engine_option.name}")

    def translate_engine_options(self, options):
        return [self.translate_engine_option(option) for option in options]

    def get_options(self):
        options = self.engine.options.values()
        options = self.translate_engine_options(options) if self.engine else []
        return list(filter(lambda x: x is not None, options))
