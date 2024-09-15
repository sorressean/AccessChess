"""
Factory that links the panel up with the games that they belong to.
"""

from accesschess.core import AIGame
from accesschess.ui.boards.ai_game_panel import AIGamePanel

registry = {
    "AI Game": (AIGame, AIGamePanel),
}


def build_components(name, parent):
    game, panel = registry[name]
    # create the game based on the object
    game = game()
    # create the panel based on the object
    panel = panel(parent, game)
    return game, panel
