targetSeqStrLen = 1000

F = 0
F_n = 1
F_n_1 = 0
i = 2

while len(str(F_n)) < targetSeqStrLen:
	F = F_n + F_n_1
	F_n_1 = F_n
	F_n = F

	print "n: " + str(i) + ", F_n:" + str(F_n)
	print len(str(F_n))
	i += 1