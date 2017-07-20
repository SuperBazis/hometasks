import getParam


class WriterPlain(getParam.GetParam):
    def write(self):
        fo = open("stat.file", "a+")
        fo.seek(0, 0)
        counter = len(fo.readlines())
        line = ''
        line += 'SNAPSHOT {} : '.format(counter + 1)
        line += str(self.dateVar)
        line += " : {} CPU usage percent\t".format(self.cpuVar)
        line += "{} MB available\t".format(self.memAvVar)
        line += "{} MB used\t".format(self.memUsVar)
        line += "{} MB total\t".format(self.memTotVar)
        line += "{} MB was read from disk\t".format(self.rDisk)
        line += "{} MB was writen to disk\t".format(self.wDisk)
        line += "{} MB was sent via network\t".format(self.sNet)
        line += "{} MB was received via network\n".format(self.rNet)
        fo.write(line)
        fo.close()
