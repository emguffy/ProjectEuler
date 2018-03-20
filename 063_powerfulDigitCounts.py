powerfulDigitCount = 0
n = 1
# proceed is set to True to kick off the top-level while loop.  However, it is then set to False at the beginning of each iteration of n.
# proceed is only set to True again if the loop of n acquires a powerful digit.  Otherwise, it stays False and the loop exits.
proceed = True
while proceed == True:
	#print("n: ",n)
	root = 1
	#print("root: ",root)
	proceed = False
	while len(str(root**n)) <= n:
		if len(str(root**n)) == n:
			proceed = True
			powerfulDigitCount += 1
			#print("n: %d; root: %d;" % (n,root))
			#print(root**n)
		root += 1
	n += 1	
print("Powerful Digit Count: ",powerfulDigitCount)
		