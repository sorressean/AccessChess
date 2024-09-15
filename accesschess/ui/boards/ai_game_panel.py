from accesschess.ui.board import ChessBoard


class AIGamePanel(ChessBoard):
    def __init__(self, parent, game):
        super().__init__(parent, game)
