import wx
from .board import ChessBoard

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        
        self.SetTitle("Access Chess")
        self.SetSize((500, 500))

        # Create chessboard panel
        self.board_panel = ChessBoard(self)

        # Create a sizer for layout management
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.board_panel, 1, wx.EXPAND)

        self.SetSizer(sizer)
        self.Centre()
