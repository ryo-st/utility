# coding: utf-8
topicNumbers = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X','A','B','C','D','E','F','G','Fig','L','T','M']

import sys
lines = sys.stdin.readlines()
newline=''
for line in lines:
    if len(line) != 0:
        line = line.replace('\n','')
        line = line.replace('\r','')
        newline = newline + line

newline=newline.replace('- ','')
newline=newline.replace('   ',' ')
newline=newline.replace('  ',' ')
newline=newline.replace(".",".\n")
newline=newline.replace("\n ","\n")

newline=newline.replace("e.\ng.\n","e.g.")
newline=newline.replace("i.\ne.\n","i.e.")
newline=newline.replace("et al.\n","et al.")
newline=newline.replace("Eq.\n","Eq.")

#cnumber:Chapter number(1.1,1.2,...)
cnumber = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
for number in cnumber:
    for number2 in cnumber:
        newline=newline.replace(number+'.\n'+number2,number+'.'+number2)

for topicNumber in topicNumbers:
    newline=newline.replace(topicNumber+'.\n',topicNumber+'.')

print (newline) 
