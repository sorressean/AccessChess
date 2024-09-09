import gc

import wx

from accesschess.ui import MainFrame


def main():
    gc.set_threshold(1500, 15, 15)
    app = wx.App(False)
    app.SetAppName("Access Chess")
    app.ExitOnFrameDelete = True
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()


main()
