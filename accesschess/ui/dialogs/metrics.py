import wx

from accesschess.core import MetricsCollector


class MetricsDialog(wx.Dialog):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Set dialog properties
        self.SetTitle("Process Metrics")
        self.SetSize((400, 600))
        self.SetBackgroundColour(wx.Colour(255, 255, 255))

        # Main vertical sizer
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Create a panel for metrics display
        self.metrics_panel = wx.Panel(self)
        self.metrics_panel.SetBackgroundColour(wx.Colour(240, 240, 240))
        main_sizer.Add(self.metrics_panel, 1, wx.ALL | wx.EXPAND, 10)

        # Sizer for the panel content
        panel_sizer = wx.BoxSizer(wx.VERTICAL)

        # Static text control for displaying the metrics
        self.metrics_text = wx.StaticText(self.metrics_panel, label="")
        panel_sizer.Add(self.metrics_text, 1, wx.ALL | wx.EXPAND, 5)
        self.metrics_panel.SetSizer(panel_sizer)

        # Collect metrics on initialization
        self.collect_and_show_metrics()

        # Set sizer for the dialog
        self.SetSizer(main_sizer)

    def collect_and_show_metrics(self):
        """Collect metrics and update the text control with formatted data."""
        collector = MetricsCollector()
        metrics = collector.collect_metrics()

        # Format the metrics for display
        formatted_metrics = (
            f"CPU Usage: {metrics['cpu_percent']}%\n"
            f"Memory RSS: {metrics['memory_rss'] / (1024 ** 2):.2f} MB\n"
            f"Memory VMS: {metrics['memory_vms'] / (1024 ** 2):.2f} MB\n"
            f"Uptime: {metrics['uptime'] / 60:.2f} minutes\n"
            f"Number of Threads: {metrics['num_threads']}\n"
            f"I/O Read Count: {metrics['io_read_count']}\n"
            f"I/O Write Count: {metrics['io_write_count']}\n"
            f"I/O Read Bytes: {metrics['io_read_bytes'] / (1024 ** 2):.2f} MB\n"
            f"I/O Write Bytes: {metrics['io_write_bytes'] / (1024 ** 2):.2f} MB\n"
        )

        # Update the static text with formatted metrics
        self.metrics_text.SetLabel(formatted_metrics)
