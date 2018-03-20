import math

def is_digit_factorial(num):
	sumFactorial = 0
	for digit in str(num):
		sumFactorial += math.factorial(int(digit))
		
	if sumFactorial == num:
		return True
	else:
		return False
		
		
digitFactorialSum = 0		
for candidate in range(3,math.factorial(9)*7 + 1):
	if is_digit_factorial(candidate) == True:
		print candidate
		digitFactorialSum += candidate
		
print "digitFactorialSum: " + str(digitFactorialSum)
