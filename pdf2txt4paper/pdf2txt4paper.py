# coding: utf-8
topicNumbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']

import sys
lines = sys.stdin.readlines()
newline=''
for line in lines:
    if len(line) != 0:
        line = line.replace('\n','')
        line = line.replace('\r','')
        newline = newline + line

newline=newline.replace('- ','')
newline=newline.replace(".",".\n")
newline=newline.replace("\n ","\n")

for topicNumber in topicNumbers:
    newline=newline.replace(topicNumber+'.\n',topicNumber+'.')
    
print (newline) 