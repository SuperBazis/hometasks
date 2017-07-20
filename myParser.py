import configparser


class MyParser:
    def __init__(self,filename):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(self.filename)

    def getConfig(self):
        self.type = str(self.config['common']['output'])
        self.min = int(self.config['common']['interval'])
        return self.type, self.min

