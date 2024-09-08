class ChessPiece:
    def __init__(self, name, abbreviation, unicode_symbol):
        self.name = name
        self.abbreviation = abbreviation
        self.unicode_symbol = unicode_symbol

    def __repr__(self):
        return f"{self.name} ({self.abbreviation}): {self.unicode_symbol}"


# Registry of chess pieces
registry = {
    'WK': ChessPiece('White King', 'WK', '♔'),
    'WQ': ChessPiece('White Queen', 'WQ', '♕'),
    'WR': ChessPiece('White Rook', 'WR', '♖'),
    'WB': ChessPiece('White Bishop', 'WB', '♗'),
    'WN': ChessPiece('White Knight', 'WN', '♘'),
    'WP': ChessPiece('White Pawn', 'WP', '♙'),
    'BK': ChessPiece('Black King', 'BK', '♚'),
    'BQ': ChessPiece('Black Queen', 'BQ', '♛'),
    'BR': ChessPiece('Black Rook', 'BR', '♜'),
    'BB': ChessPiece('Black Bishop', 'BB', '♝'),
    'BN': ChessPiece('Black Knight', 'BN', '♞'),
    'BP': ChessPiece('Black Pawn', 'BP', '♟')
}
