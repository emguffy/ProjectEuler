rangeMax = 101

sumOfSquares = 0
for i in range(1,rangeMax):
	sumOfSquares += i**2
	
sums = 0
for j in range(1,rangeMax):
	sums += j

squareOfSums = sums**2

sumSquareDifference = squareOfSums - sumOfSquares
print sumSquareDifference