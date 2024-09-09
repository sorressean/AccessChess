import wx
from .board import ChessBoard
from .component_factory import build_components

class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        self.game = None
        self.board_panel = None
        self.game_menu = None  # Track the game-specific menu
        super(MainFrame, self).__init__(*args, **kw)
        self.SetTitle("Access Chess")
        self.SetSize((600, 600))
        self.create_menubar()

    def create_board(self, game_name):
        # Clear existing board if one exists
        if self.board_panel:
            self.board_panel.Destroy()
            self.board_panel = None
                # Remove the existing game menu if any
        self.clear_game_menu()

        self.game_menu = wx.Menu()
        game,panel = build_components(game_name, self, self.game_menu)
        self.game = game
        self.board_panel = panel
        self.GetMenuBar().Append(self.game_menu, "&Game")
        # Create a sizer for layout management
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.board_panel, 1, wx.EXPAND)
        self.SetSizer(sizer)
        self.Layout()  # Make sure the layout refreshes to show the new panel
        self.game.on_new_game()
        self.Centre()

    def create_menubar(self):
        menubar = wx.MenuBar()

        # File menu
        file_menu = wx.Menu()
        
        # New submenu
        new_game_menu = wx.Menu()
        new_ai_game = wx.MenuItem(new_game_menu, wx.ID_NEW, 'New &AI Game')
        new_game_menu.Append(new_ai_game)
        file_menu.Append(wx.ID_ANY, '&New', new_game_menu)

        # Exit option
        exit_item = wx.MenuItem(file_menu, wx.ID_EXIT, 'Exit\tCtrl+Q')
        file_menu.Append(exit_item)

        # Bind the events to methods
        self.Bind(wx.EVT_MENU, self.on_new_ai_game, new_ai_game)
        self.Bind(wx.EVT_MENU, self.on_exit, exit_item)

        menubar.Append(file_menu, '&File')
        self.SetMenuBar(menubar)

    def clear_game_menu(self):
        """
        Clears the game-specific menu if it exists.
        """
        if self.game_menu:
            menubar = self.GetMenuBar()
            menubar.Remove(menubar.FindMenu(self.game_menu.GetTitle()))
            self.game_menu = None

    def on_new_ai_game(self, event):
        # Handle starting a new AI game
        self.create_board('AI Game')

    def on_exit(self, event):
        self.Close()
