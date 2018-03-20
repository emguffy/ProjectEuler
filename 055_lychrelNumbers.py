def is_palindrome(candidate):
	if candidate == int(str(candidate)[::-1]):
		return True
	else:
		return False

def reverse_int(n):
	return int(str(n)[::-1])

lychrelList = []
for number in range(1,10001):
	isLychrel = True
	i = 1
	while i <= 50:
		number += reverse_int(number)
		if is_palindrome(number):
			isLychrel = False
			break
		else:
			i += 1
	
	if isLychrel:
		lychrelList.append(number)
		
print(lychrelList)
print("Count: ",len(lychrelList))
			
