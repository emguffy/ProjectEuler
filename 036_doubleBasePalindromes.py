palindromeList = []

def is_palindrome(numStr):
	numberLength = len(numStr)
	i = 0
	isPalindrome = True
	while i < numberLength/2:
		if numStr[i] != numStr[numberLength - 1 - i]:
			isPalindrome = False
			break
		else:
			i += 1
	
	return isPalindrome
	
for number in range(1,1000001):
	if is_palindrome(str(number)) and is_palindrome(bin(number)[2:]):
		palindromeList.append(number)
		print "number: " + str(number)
		
		
print "sum(palindromeList): " + str(sum(palindromeList))
