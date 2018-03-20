
permutationFound = False
number = 100000


while permutationFound == False:
	for multiple in range(2,7):
		if sorted(str(number*multiple)) != sorted(str(number)):
			permutationFound = False
			break
	else:
		permutationFound = True
		print("number: ",number)
		print("number x 2: ",number*2)
		print("number x 3: ",number*3)
		print("number x 4: ",number*4)
		print("number x 5: ",number*5)
		print("number x 6: ",number*6)
	
	number += 1

