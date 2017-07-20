import json
import getParam


class WriterJSON(getParam.GetParam):
    def write(self):
        self.fo = open("stat.json", "a+")
        self.fo.seek(0,0)
        self.counter = len(self.fo.readlines())
        if self.counter == 0:
            self.snapVar = 'SNAPSHOT {}'.format(1)
            self.pythonDictionary = {
                self.snapVar:{'Timestamp':self.dateVar,'CPU':self.cpuVar,'MemoryAvailable':self.memAvVar,
                              'MemoryUsed':self.memUsVar,'MemoryTotal':self.memTotVar,'ReadDisk':self.rDisk,
                              'WriteDisk':self.wDisk, 'SentNet':self.sNet,'ReceiveNet':self.rNet}}
            json.dump(self.pythonDictionary,self.fo, indent=4)

        else:
            with open('stat.json') as f:
                self.data = json.load(f)
            self.snapVar = 'SNAPSHOT {}'.format(len(self.data) + 1)
            self.pythonDictionary = {
                self.snapVar: {'Timestamp': self.dateVar, 'CPU': self.cpuVar, 'MemoryAvailable': self.memAvVar,
                               'MemoryUsed': self.memUsVar, 'MemoryTotal': self.memTotVar, 'ReadDisk': self.rDisk,
                               'WriteDisk': self.wDisk, 'SentNet': self.sNet, 'ReceiveNet': self.rNet}}
            self.data.update(self.pythonDictionary)

            with open('stat.json', 'w') as f:
                json.dump(self.data, f, indent=4)
        self.fo.close()
