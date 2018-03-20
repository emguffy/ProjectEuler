# The largest number that is a permutation of 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9 is 9876543210
# The smallest number is 123456789

# There are 10 factorial = 3628800 permutations

# A brute force method could be to iterate through each number from 123456789 to 9876543210, checking whether each number was a permutation.
# Using a counter, we could then stop at the 1,000,000th permutation

# Another method would be to build a list of all permuations, then order the list and find the 1,000,000th member
# With a list 3,628,800 members long, this would also be a lengthy algorithm

# The best method would find a way to seek the next ordered permutation from a current permutation.
# If the first permutation is 0123456789, the next is 0123456798
# next is 0123456879
# next is 0123456897
# next is 0123457689
# next is 0123457698


# First, lets see how long it would take to do a brute force calculation
# Perhaps we can install some rules that will help speed up the process

permutationTarget = 1000000
permutationCounter = 1
minPermutation = 123456789
maxPermutation = 9876543210


def nextPermutation(num):
	if "0" not in str(num):
		listNum = list("0" + str(num))
	else:
		listNum = list(str(num))
		
	pointer1 = len(listNum) - 1
	pointer2 = pointer1
	while pointer1 > 0:
		if listNum[pointer1] > listNum[pointer1 - 1]:
			while pointer2 >= pointer1:
				if listNum[pointer2] > listNum[pointer1 - 1]:
					listMarker = listNum[pointer1 - 1]
					listNum[pointer1 - 1] = listNum[pointer2]
					listNum[pointer2] = listMarker
					listNum[pointer1:] = sorted(listNum[pointer1:])
					
					pointer2 = 0
				else:	
					pointer2 -= 1
				
			strNextPermutation = ""
			for item in listNum:
				strNextPermutation = strNextPermutation + item
				
			pointer1 = 0
		else:
			pointer1 -= 1
	
	return int(strNextPermutation)




pointer = minPermutation
while permutationCounter <= permutationTarget and pointer < maxPermutation:
	print str(permutationCounter) + ", " + str(pointer)
	permutationCounter += 1
	pointer = nextPermutation(pointer)
	
print str(permutationCounter) + ", " + str(pointer)

	
			
	