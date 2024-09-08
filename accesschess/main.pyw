import wx
from accesschess.ui import MainFrame

if __name__ == "__main__":
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()
