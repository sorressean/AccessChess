import wx

from accesschess.core.options import OptionType


class AIEngineOptionsDialog(wx.Dialog):
    def __init__(self, parent, game):
        super().__init__(parent, title="Engine Options", size=(400, 600))
        print("show dialog.")
        self.game = game
        self.options_controls = {}  # Store the input controls for each option
        # Retrieve engine options
        options = self.game.get_options()
        print(options)
        # Initialize the sizer for layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)
        # Create a grid sizer for the options
        rows = len(options)
        grid_sizer = wx.FlexGridSizer(rows, cols=2, hgap=10, vgap=10)
        grid_sizer.AddGrowableCol(1, 1)  # Make the input fields expand

        # Iterate through the options and create input controls based on type
        for option in options:
            label = wx.StaticText(self, label=option.name)
            grid_sizer.Add(label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            control = None
            # Create controls based on the type of option
            if option.type == OptionType.Boolean:
                control = wx.CheckBox(self)
                control.SetValue(option.metadata.get("default", False))
            elif option.type == OptionType.Number:
                control = wx.SpinCtrl(self, value=str(option.metadata.get("default", 0)))
                control.SetRange(option.metadata.get("min", 0), option.metadata.get("max", 100))
            elif option.type == OptionType.String:
                control = wx.TextCtrl(self, value=option.metadata.get("default", ""))

            # Add the control to the sizer and keep track of it
            if control:
                grid_sizer.Add(control, 1, wx.EXPAND | wx.ALL, 5)
                self.options_controls[option.name] = control

        main_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 10)

        # Add Ok and Cancel buttons
        button_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(main_sizer)
        self.Layout()
        self.Center()

        # Bind events
        self.Bind(wx.EVT_BUTTON, self.on_ok, id=wx.ID_OK)

    def on_ok(self, event):
        # Apply the updated options to the game engine
        for option_name, control in self.options_controls.items():
            if isinstance(control, wx.CheckBox):
                new_value = control.GetValue()
            elif isinstance(control, wx.SpinCtrl):
                new_value = control.GetValue()
            elif isinstance(control, wx.TextCtrl):
                new_value = control.GetValue()

            # Set the new value for the option in the game
            self.game.set_option(option_name, new_value)

        self.EndModal(wx.ID_OK)
