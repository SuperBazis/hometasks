import myParser
import writerJSON
import writerPlain
import time

pars = myParser.MyParser('settings.ini')
params = pars.getConfig()
if params[0] == 'json':
    while True:
        obj = writerJSON.WriterJSON()
        obj.write()
        time.sleep(params[1] * 60)
elif params[0] == 'plain':
    while True:
        obj = writerPlain.WriterPlain()
        obj.write()
        time.sleep(params[1] * 60)
