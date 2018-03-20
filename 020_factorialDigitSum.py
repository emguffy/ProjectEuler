import math

factorial100 = str(math.factorial(100))
print factorial100

sumFactorial100 = 0
for digit in factorial100:
	sumFactorial100 += int(digit)
	
print sumFactorial100

