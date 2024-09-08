import wx
from accesschess.ui import ChessBoard
from accesschess.ui.dialogs import AIEngineOptionsDialog

class AIGamePanel(ChessBoard):
    def __init__(self, parent, menubar, game):
        super().__init__(parent, menubar, game)
        options_item = wx.MenuItem(menubar, wx.ID_ANY, "Engine &Options")
        menubar.Append(options_item)
        self.Bind(wx.EVT_MENU, self.on_options, options_item)

    def on_options(self, event):
        dialog = AIEngineOptionsDialog(self, self.game)
        dialog.ShowModal()
        dialog.Destroy()    