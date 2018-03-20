# combinatoric selectors
		
def combinatorial(n,r):	
	nFactorial = n
	for nFactor in range(1,n):
		nFactorial *= nFactor
		
	rFactorial = r
	for rFactor in range(1,r):
		rFactorial *= rFactor
		
	nMrFactorial = n - r
	for nMrFactor in range(1,n-r):
		nMrFactorial *= nMrFactor
		
	return nFactorial / (rFactorial * nMrFactorial)

c1MCount = 0
	
for n in range(1,101):
	for r in range(1,n):
		combo = combinatorial(n,r)
		print ("n: ",n,", r: ",r,", combinatorial: ",combo)
		if combo > 1000000:
			c1MCount += 1
		
print("c1MCount: ",c1MCount)