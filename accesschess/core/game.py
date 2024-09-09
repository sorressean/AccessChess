"""
Main game object.
"""
import chess
from .sound_manager import sound

class Game:
    def __init__(self):
        self.initialize_game()

    def initialize_game(self):
        self.board = chess.Board()
        self.callback = None

    def set_ui_callback(self, callback):
        self.callback = callback

    def get_grid_mapping(self):
        board = [['' for _ in range(8)] for _ in range(8)]
        for square in chess.SQUARES:
            piece = self.board.piece_at(square)
            if piece is None: continue
            row = square//8
            column = square%8
            board[row][column]=piece.unicode_symbol()
        return board

    def get_options(self):
        return {}
    def on_new_game(self):
        #play a new game sound.
        sound.play_sound('new_game')
