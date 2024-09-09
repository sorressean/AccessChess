import wx


class ChessBoard(wx.Panel):
    def __init__(self, parent, menubar, game):
        super().__init__(parent)
        self.selected_piece = None
        self.selected_square = None
        self.buttons = {}
        self.game = game
        self.create_board()

    def create_board(self):
        # Create an 8x8 grid for the chessboard
        grid_sizer = wx.GridSizer(8, 8, 0, 0)

        initial_board = self.game.get_grid_mapping()
        # Build the board with alternating colors and assign pieces
        for row in range(8):
            for col in range(8):
                square_id = (row, col)
                label = initial_board[row][col]

                # Create a button for each square
                button = wx.Button(self, label=label, size=(50, 50))
                if (row + col) % 2 == 0:
                    button.SetBackgroundColour(wx.Colour(240, 217, 181))
                else:
                    button.SetBackgroundColour(wx.Colour(181, 136, 99))

                # Bind mouse events
                button.Bind(wx.EVT_BUTTON, self.on_square_click)

                # Add button to grid and store it in buttons dict
                grid_sizer.Add(button, 0, wx.EXPAND)
                self.buttons[square_id] = button

        self.SetSizer(grid_sizer)
        self.Layout()

    def on_square_click(self, event):
        # Identify which button was clicked
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
