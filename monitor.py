import psutil
import datetime
import time
import configparser
import json
config = configparser.ConfigParser()
config.read('settings.ini')
type = str(config['common']['output'])
min = int(config['common']['interval'])
if type == 'plain':
    while True:
        fo = open("stat.file", "a+")
        fo.seek(0,0)
        counter = len(fo.readlines())
        line = ''
        line += 'SNAPSHOT {} : '.format(counter+1)
        line += str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        line += " : {} CPU usage percent\t".format(psutil.cpu_percent(interval=0.1))
        line += "{} MB available\t".format(psutil.virtual_memory().available//1024//1024)
        line += "{} MB used\t".format(psutil.virtual_memory().used//1024//1024)
        line += "{} MB total\t".format(psutil.virtual_memory().total//1024//1024)
        line += "{} MB was read from disk\t".format(psutil.disk_io_counters().read_bytes //1024//1024)
        line += "{} MB was writen to disk\t".format(psutil.disk_io_counters().write_bytes //1024//1024)
        line += "{} MB was sent via network\t".format(psutil.net_io_counters(pernic=True)['eno1'].bytes_sent//1024//1024)
        line += "{} MB was received via network\n".format(psutil.net_io_counters(pernic=True)['eno1'].bytes_recv//1024//1024)
        fo.write(line)
        fo.close()
        time.sleep(min*60)
if type == 'json':
    while True:
        fo = open("stat.json", "a+")
        fo.seek(0,0)
        counter = len(fo.readlines())
        if counter == 0:
            snapVar = 'SNAPSHOT {}'.format(counter+1)
            dateVar = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cpuVar = psutil.cpu_percent(interval=0.1)
            memAvVar = psutil.virtual_memory().available//1024//1024
            memUsVar = psutil.virtual_memory().used//1024//1024
            memTotVar = psutil.virtual_memory().total//1024//1024
            rDisk= psutil.disk_io_counters().read_bytes //1024//1024
            wDisk = psutil.disk_io_counters().write_bytes //1024//1024
            sNet = psutil.net_io_counters(pernic=True)['eno1'].bytes_sent//1024//1024
            rNet = psutil.net_io_counters(pernic=True)['eno1'].bytes_recv//1024//1024
            pythonDictionary = {snapVar:{'Timestamp':dateVar,'CPU':cpuVar,'MemoryAvailable':memAvVar,'MemoryUsed':memUsVar,\
                                        'MemoryTotal':memTotVar, 'ReadDisk':rDisk, 'WriteDisk':wDisk, 'SentNet':sNet, 'ReceiveNet':rNet}}
            json.dump(pythonDictionary,fo, indent=4)

        else:
            with open('stat.json') as f:
                data = json.load(f)

            snapVar = 'SNAPSHOT {}'.format(len(data) + 1)
            dateVar = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            cpuVar = psutil.cpu_percent(interval=0.1)
            memAvVar = psutil.virtual_memory().available // 1024 // 1024
            memUsVar = psutil.virtual_memory().used // 1024 // 1024
            memTotVar = psutil.virtual_memory().total // 1024 // 1024
            rDisk = psutil.disk_io_counters().read_bytes // 1024 // 1024
            wDisk = psutil.disk_io_counters().write_bytes // 1024 // 1024
            sNet = psutil.net_io_counters(pernic=True)['eno1'].bytes_sent // 1024 // 1024
            rNet = psutil.net_io_counters(pernic=True)['eno1'].bytes_recv // 1024 // 1024
            pythonDictionary = {
                snapVar: {'Timestamp': dateVar, 'CPU': cpuVar, 'MemoryAvailable': memAvVar, 'MemoryUsed': memUsVar, \
                          'MemoryTotal': memTotVar, 'ReadDisk': rDisk, 'WriteDisk': wDisk, 'SentNet': sNet,
                          'ReceiveNet': rNet}}
            data.update(pythonDictionary)

            with open('stat.json', 'w') as f:
                json.dump(data, f, indent=4)
        fo.close()
        time.sleep(min*60)