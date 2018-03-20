
matchFound = False
n = 0
tList = []
pList = []
hList = []

while matchFound == False:
	tList.append(n*(n+1)/2)
	pList.append(n*(3*n-1)/2)
	hList.append(n*(2*n-1))
	
	
	if n > 285:
		if tList[n] in pList and tList[n] in hList:
			matchFound = True
			print "n: " + str(n)
			print "tList[n]: " + str(tList[n])
			
	n += 1