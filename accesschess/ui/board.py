import wx


class ChessBoard(wx.Panel):
    def __init__(self, parent):
        super().__init__(parent)
        self.selected_piece = None
        self.selected_square = None
        self.buttons = {}
        self.focused_square = (0, 0)  # Track focused square for arrow key navigation
        self.captured_white_pieces = []  # Store captured white pieces
        self.captured_black_pieces = []  # Store captured black pieces
        self.create_ui()

    def create_ui(self):
        main_sizer = wx.BoxSizer(wx.HORIZONTAL)

        # Left column for captured white pieces
        white_captured_sizer = wx.BoxSizer(wx.VERTICAL)
        white_captured_label = wx.StaticText(self, label="Captured White Pieces")
        white_captured_sizer.Add(white_captured_label, 0, wx.CENTER | wx.TOP, 10)
        self.white_captured_list = wx.ListBox(self, size=(80, 300))
        white_captured_sizer.Add(self.white_captured_list, 1, wx.EXPAND | wx.ALL, 10)
        main_sizer.Add(white_captured_sizer, 1, wx.EXPAND | wx.ALL, 10)

        # Right column for captured black pieces
        black_captured_sizer = wx.BoxSizer(wx.VERTICAL)
        black_captured_label = wx.StaticText(self, label="Captured Black Pieces")
        black_captured_sizer.Add(black_captured_label, 0, wx.CENTER | wx.TOP, 10)
        self.black_captured_list = wx.ListBox(self, size=(80, 300))
        black_captured_sizer.Add(self.black_captured_list, 1, wx.EXPAND | wx.ALL, 10)
        # created the right column, but add it after the board.

        chessboard_sizer = wx.BoxSizer(wx.VERTICAL)
        # Top row with coordinates (a-h)
        top_coord_sizer = wx.BoxSizer(wx.HORIZONTAL)
        top_coord_sizer.AddSpacer(40)  # Space before the first column label
        for letter in "abcdefgh":
            top_coord_sizer.Add(wx.StaticText(self, label=letter), 1, wx.CENTER)
        chessboard_sizer.Add(top_coord_sizer, 0, wx.EXPAND)

        # Main grid for the chessboard
        grid_sizer = wx.GridSizer(9, 8, 0, 0)
        initial_board = self.game.get_grid_mapping()
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.BOLD)  # Set larger font for buttons

        for row in range(8):
            # Add left-side row numbers (1-8)
            row_label = wx.StaticText(self, label=str(8 - row))  # Row numbers (8 to 1)
            grid_sizer.Add(row_label, 0, wx.EXPAND)
            # Build the chessboard grid with alternating colors and pieces
            for col in range(8):
                square_id = (row, col)
                label = initial_board[row][col]
                button = wx.Button(self, label=label, size=(50, 50))
                button.SetFont(font)  # Increase font size
                button.SetName(self.get_square_name(row, col))  # Set chess coordinate as name
                # Set alternating square colors
                if (row + col) % 2 == 0:
                    button.SetBackgroundColour(wx.Colour(240, 217, 181))  # Light square
                else:
                    button.SetBackgroundColour(wx.Colour(181, 136, 99))  # Dark square
                # Bind button events
                button.Bind(wx.EVT_BUTTON, self.on_square_click)
                grid_sizer.Add(button, 0, wx.EXPAND)
                self.buttons[square_id] = button
        chessboard_sizer.Add(grid_sizer, 0, wx.EXPAND | wx.ALL, 10)
        main_sizer.Add(chessboard_sizer, 1, wx.EXPAND | wx.ALL, 10)
        main_sizer.Add(black_captured_sizer, 1, wx.EXPAND | wx.ALL, 10)
        self.SetSizer(main_sizer)
        self.Layout()
        self.Center()

    def get_square_name(self, row, col):
        # Create a chess-style coordinate system (a1, h8, etc.)
        letters = "abcdefgh"
        numbers = "87654321"
        return f"{letters[col]}{numbers[row]}"

    def on_square_click(self, event):
        clicked_button = event.GetEventObject()

        # Determine which square was clicked based on the button reference
        clicked_square = None
        for square, button in self.buttons.items():
            if button == clicked_button:
                clicked_square = square
                break

        if self.selected_piece is None:
            # Select a piece if one isn't already selected
            if clicked_button.GetLabel():
                self.selected_piece = clicked_button.GetLabel()
                self.selected_square = clicked_square
                clicked_button.SetLabel("")
        else:
            # Move the selected piece to the new square
            clicked_button.SetLabel(self.selected_piece)
            self.selected_piece = None
            self.selected_square = None

        # Simulate piece capture for demo purposes
        self.simulate_piece_capture(clicked_button.GetLabel())

    def simulate_piece_capture(self, piece):
        if piece:
            if piece.islower():  # Lowercase pieces are black
                self.white_captured_list.Append(piece.upper())  # Append captured black piece to white's captured list
            else:
                self.black_captured_list.Append(piece.lower())  # Append captured white piece to black's captured list

    def on_new_game(self):
        pass
