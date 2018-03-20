combos = []

for a in range(2,101):
	for b in range(2,101):
		combos.append(a**b)

combos = sorted(set(combos))
print len(combos)