import re
lines = open("keys3.txt").readlines()
filein = open("addto3.txt", "a")
for line in lines:
    line = line.lstrip()
    line = line.replace("(u'","")
    line = line.replace("\\x08","")
    line = line.replace(":',)(\"'"," ")
    line = line.replace("\\\\\\\\\\\\\\\\'\", ',')'"," ")
    line = line.replace(":',)(\"'","\n")
    line = line.replace("\\x05","");line = line.replace("\\x03","");line = line.replace("\\x06","")
    line = line.replace(":',)(\"'","\n")
    line = line.replace("\\\\\'\", ',')'","  ")
    line = line.replace("\\x07"," ")
    line = line.replace("\\x04","  ")
    line = line.replace("\  \  \  \  '\", ',')'","  ")
    line = line.replace("\\","  ");line = line.replace("'","")
    line = line.replace("\", ,)","");line = line.replace("x02","")
    line = line.replace("x01","");line = line.replace("x01","")
    line = re.sub(' +',' ',line)
    filein.write(line)
filein.close()    