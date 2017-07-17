rezultDict = {}
with open('access.log', 'r') as http:
    for line in http:
        line = line.split(' ')
        if (not line[0] in rezultDict.keys()):
            rezultDict[line[0]] = 1
        else:
            rezultDict[line[0]] = rezultDict[line[0]] + 1
b = list(rezultDict.items())
b.sort(key=lambda item: item[1], reverse=True)
if len(b) < 10:
    Counter = len(b)
else:
    Counter = 10
for i in range(Counter):
    print(b[i][0])