targetSum = 1000
answer = 0
k = 0
		
print "targetSum/3 = " + str(targetSum/3)

# First make a list of all potential triplets that add up to 1000
for i in range(1,targetSum/3):
	# print "i: " + str(i)
	for j in range(i + 1,(targetSum-i)/2 + 1):
		# print "j: " + str(j)
		k = targetSum - i - j
		# print "k: " + str(k)
		if (i**2 + j**2 == k**2):
			print i+j+k
			print i*j*k
			
		
		
		# print str(i) + str(j) + str(k) + str(i + j + k)
		
	