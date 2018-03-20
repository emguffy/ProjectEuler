
selfPowerSum = 0
for num in range(1,1001):
	selfPowerSum += num**num
	
print "Last 10 digits: " + str(selfPowerSum)[len(str(selfPowerSum))-10:]
