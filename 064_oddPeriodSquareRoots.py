import math

def expand(square,remainder,denom):
	""" Returns a tuple of the rootFloor and the remainder. """
	floorVal = math.floor((math.sqrt(square) + remainder)/denom)
	newRemainder = floorVal * denom - remainder
	newDenom = int((square - newRemainder**2)/denom)
	return(floorVal,square,newRemainder,newDenom)

bottomRange = 1
topRange = 10001
oddPeriodCount = 0
for N in range(bottomRange,topRange):
	continueList = []
	
	# initializing values for each N
	sq = N
	rmndr = 0
	dnm = 1
	if int(math.sqrt(N))**2 != N:
		while True:
			expTup = expand(sq,rmndr,dnm)
			# print(N," ",expTup)
			if expTup in continueList:
				period = len(continueList) - continueList.index(expTup)
				break
			else:
				continueList.append(expTup)
				rmndr = expTup[2]
				dnm = expTup[3]
		#print("period: ",period)
		if period % 2 == 1:
			#print('N: %s; Period: %s' % (N,period))
			oddPeriodCount += 1


print("oddPeriodCount: ",oddPeriodCount)