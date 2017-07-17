keylist = ['key1','key2','key3','key4','key5']
#valuelist = ['value1', 2, 3, 4, 5]
#valuelist = ['value1', 2, 3, 4]
valuelist = ['value1', 45, 3, 4, 5, 6]
keyLength = len(keylist)
valueLength = len(valuelist)
rezultDict = {}
for i in range(keyLength):
    if i<=valueLength-1:
        rezultDict[keylist[i]] = valuelist[i]
    else:
        rezultDict[keylist[i]] = None
print(rezultDict)