import os
import itertools

xorFile = open("/Users/DeskGuff/Documents/Programming/PEProblems/XORDecryption.txt",'r')
xorData = xorFile.read()

l1 = []
l2 = []
l3 = []
for index, ascii in enumerate(xorData.split(',')):
	if index % 3 == 0:
		l1.append(int(ascii.strip()))
	if index % 3 == 1:
		l2.append(int(ascii.strip()))
	if index % 3 == 2:
		l3.append(int(ascii.strip()))
	
freq1 = {x:l1.count(x) for x in l1}
v=list(freq1.values())
k=list(freq1.keys())
encl1Space = k[v.index(max(v))]

freq2 = {x:l2.count(x) for x in l2}
v=list(freq2.values())
k=list(freq2.keys())
encl2Space = k[v.index(max(v))]

freq3 = {x:l3.count(x) for x in l3}
v=list(freq3.values())
k=list(freq3.keys())
encl3Space = k[v.index(max(v))]
print(freq3)
print(encl3Space)

i = 32
cipher1 = 32 ^ encl1Space
cipher2 = 32 ^ encl2Space
cipher3 = 32 ^ encl3Space
cipher = [chr(cipher1),chr(cipher2),chr(cipher3)]
print(''.join(cipher))

asciiTrue = []
for index, ascii in enumerate(xorData.split(',')):
	if index % 3 == 0:
		asciiTrue.append(chr(int(ascii)^cipher1))
	if index % 3 == 1:
		asciiTrue.append(chr(int(ascii)^cipher2))
	if index % 3 == 2:
		asciiTrue.append(chr(int(ascii)^cipher3))

message = ''.join(asciiTrue)
print (message)

asciiSum = 0
for char in message:
	asciiSum += ord(char)
	
print("asciiSum: ", asciiSum)
	
xorFile.close