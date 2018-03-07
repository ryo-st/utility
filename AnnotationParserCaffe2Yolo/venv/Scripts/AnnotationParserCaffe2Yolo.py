import sys
import os
m=os.getcwd()
argv = sys.argv

path=os.path.join(os.path.dirname(os.path.dirname(m)),"Data")

afterPath=os.path.join(path,"After")
if not os.path.exists(afterPath):
    os.mkdir(afterPath)

files=os.listdir(path)
for file in files:
    filepath=os.path.join(path,file)
    readFile = open(filepath)
    data=readFile.read()
    data=data.replace(' ','')
    while data[0] == '[' and data[-1]==']':
        data = data[1:-1]
    data=data.split(']')
    for d_index in range(len(data)):
        if data[d_index][0:2] == ",[":
            data[d_index] = data[d_index][2:]
    result=""
    for d in data:
        print(d)
        d=d.split(',')
        width = int(d[2]) - int(d[0])
        heigh = int(d[3]) - int(d[1])
        xPos = int(d[0]) + int(width/2)
        yPos = int(d[1]) + int(heigh/2)
        # for debug
        if(d[4] != "'grape'"):
            print("It is not grape label.")
            sys.exit()

        if(result != ""):result=result+"\n"
        result = result+"0 "+str(xPos)+" "+str(yPos)+" "+str(width)+" "+str(heigh)
    print(result)
    writeFile = open(os.path.join(afterPath,file),'w')
    writeFile.write(result)
    writeFile.close()


