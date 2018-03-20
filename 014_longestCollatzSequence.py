""" My way
maxStart = 1000000

longestSequence = 0
longestStart = 0

for start in range(1,maxStart):
	pointer = start
	sequence = 1
	while (pointer != 1):
		if pointer % 2 == 0:
			pointer /= 2
		else:
			pointer = pointer * 3 + 1
		sequence += 1
		
	if sequence > longestSequence:
		longestSequence = sequence
		longestStart = start
		print start
"""
		
		
		
import operator

def collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return (3*n + 1)

candidates = range(1, 1000000)
sequence_lens = {}

for candidate in candidates:
    n = candidate
    seq = []
    seq_length = 0
    while n != 1:
        seq.append(n)
		
        if n in sequence_lens:
            seq_length += sequence_lens[n]
			print seq_length
            for i in xrange(len(seq) - 1):
                sequence_lens[seq[i]] = seq_length - i
            break
        seq_length += 1
        n = collatz(n)
		
		
    if candidate not in sequence_lens:
        sequence_lens[candidate] = seq_length

	print sequence_lens


reduced_sequence_lens = {key: value for key,value in sequence_lens.items() if key < 1000000}

print "longest chain",  max(reduced_sequence_lens.iteritems(), key=operator.itemgetter(1))[0]