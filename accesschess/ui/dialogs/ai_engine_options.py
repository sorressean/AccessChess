import wx


class AIEngineOptionsDialog(wx.Dialog):
    def __init__(self, parent, game):
        super().__init__(parent, title="Engine Options", size=(400, 600))
        self.game = game
        self.options_controls = {}  # Store the input controls for each option

        # Retrieve engine options
        options = self.game.get_options()

        # Initialize the sizer for layout
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a grid sizer for the options
        rows = len(options)
        grid_sizer = wx.FlexGridSizer(rows, cols=2, hgap=10, vgap=10)
        grid_sizer.AddGrowableCol(1, 1)  # Make the input fields expand

        # Iterate through the options and create input controls based on type
        for option_name, option_value in options.items():
            label = wx.StaticText(self, label=option_name)
            grid_sizer.Add(label, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALL, 5)

            # Choose the appropriate control based on the type of the option
            if isinstance(option_value, bool):
                control = wx.CheckBox(self)
                control.SetValue(option_value)
            elif isinstance(option_value, int):
                control = wx.SpinCtrl(self, value=str(option_value))
            elif isinstance(option_value, float):
                control = wx.TextCtrl(self, value=str(option_value))
            else:
                control = wx.TextCtrl(self, value=str(option_value))

            grid_sizer.Add(control, 1, wx.EXPAND | wx.ALL, 5)
            self.options_controls[option_name] = control
        main_sizer.Add(grid_sizer, 1, wx.EXPAND | wx.ALL, 10)

        # Add Ok and Cancel buttons
        button_sizer = self.CreateButtonSizer(wx.OK | wx.CANCEL)
        main_sizer.Add(button_sizer, 0, wx.ALIGN_CENTER | wx.ALL, 10)

        self.SetSizer(main_sizer)
        self.Layout()

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
                try:
                    # Try converting to float if needed
                    new_value = float(new_value)
                except ValueError:
                    pass  # Leave it as string if conversion fails

            # Set the new value for the option
            self.game.set_option(option_name, new_value)
        self.EndModal(wx.ID_OK)
