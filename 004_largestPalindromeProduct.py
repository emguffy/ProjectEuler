

def is_palindrome(candidate):
	if candidate == int(str(candidate)[::-1]):
		return True
	else:
		return False

palindromePointer = 0	
threeDigitList = range(100,1000)

for x in threeDigitList:
	for y in threeDigitList:
		if is_palindrome(x*y) == True:
			if x*y > palindromePointer:
				palindromePointer = x*y

print "palindromePointer: " + str(palindromePointer) 