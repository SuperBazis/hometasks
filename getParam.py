import datetime
import psutil


class GetParam:


    def __init__(self):

        self.dateVar = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.cpuVar = psutil.cpu_percent(interval=1)
        self.memAvVar = psutil.virtual_memory().available // 1024 // 1024
        self.memUsVar = psutil.virtual_memory().used // 1024 // 1024
        self.memTotVar = psutil.virtual_memory().total // 1024 // 1024
        self.rDisk = psutil.disk_io_counters().read_bytes // 1024 // 1024
        self.wDisk = psutil.disk_io_counters().write_bytes // 1024 // 1024
        self.sNet = psutil.net_io_counters(pernic=True)['eno1'].bytes_sent // 1024 // 1024
        self.rNet = psutil.net_io_counters(pernic=True)['eno1'].bytes_recv // 1024 // 1024
