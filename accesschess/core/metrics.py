import time

import psutil


class MetricsCollector:
    def __init__(self):
        self.process = psutil.Process()

    def collect_metrics(self):
        """Collect various metrics for the current process."""
        metrics = {}

        # Collect CPU usage percentage
        metrics["cpu_percent"] = self.process.cpu_percent(interval=1)

        # Collect memory usage
        memory_info = self.process.memory_info()
        metrics["memory_rss"] = memory_info.rss  # Resident Set Size
        metrics["memory_vms"] = memory_info.vms  # Virtual Memory Size

        # Collect process uptime
        metrics["uptime"] = time.time() - self.process.create_time()

        # Collect number of threads
        metrics["num_threads"] = self.process.num_threads()

        # Collect process I/O counters
        io_counters = self.process.io_counters()
        metrics["io_read_count"] = io_counters.read_count
        metrics["io_write_count"] = io_counters.write_count
        metrics["io_read_bytes"] = io_counters.read_bytes
        metrics["io_write_bytes"] = io_counters.write_bytes
        return metrics
