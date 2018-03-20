# Pentegon NUmbers

def is_pentagon(number):
	isPentagon = False
	for n in range( int(2*(number**.5)/3) , int(number**.5)+1):
		if number == n*(3*n - 1)/2:
			print n
			isPentagon = True
			break
	return isPentagon

print int(2167*(3*2167 - 1)/2)
print is_pentagon(7042750)
print is_pentagon(1560090)
print is_pentagon(7042750 + 1560090)
print is_pentagon(7042750 - 1560090)
print 7042750 - 1560090

'''
# pDist represents the difference between the next member of the pentagonList and the previous member
# Once this distance is greater than D, the distance of a found pair, we know we won't be able to find
# a pair of pentagon numbers of lesser distance.	
# Initially, we set the pDist to 0, but we'll re-initialize it once we find a pPair.
pDist = 0
D = 0
pentagonList = [1]
n = 2
while D==0 or pDist < D:
	pentagonList.append(n*(3*n-1)/2)
	pDist = pentagonList[n-1] - pentagonList[n-2]
	#print "pentagonList[n-2]: " + str(pentagonList[n-2])
	for j in range(0,n-1):
		#raw_input("type something")
		#print pentagonList[n-1] - pentagonList[j]
		#print pentagonList[n-1] + pentagonList[j]
		if is_pentagon(pentagonList[n-1] - pentagonList[j]) and is_pentagon(pentagonList[n-1] + pentagonList[j]):
			print "found one: " + str(pentagonList[n-1]) + ' ' + str(pentagonList[j])
			dist = pentagonList[n-1] + pentagonList[j]
			if dist < D or D==0:
				D = dist
	n += 1

'''