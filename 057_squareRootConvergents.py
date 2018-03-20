# This is a recursive problem

def square_two(expansions):
	i = expansions
	numerator = 2
	denominator = 1
	while i > 1:
		denom = numerator
		numerator = 2 * numerator + denominator
		denominator = denom
		i -= 1
		
	denom = numerator
	numerator = numerator + denominator
	denominator = denom

	return {'numerator':numerator, 'denominator':denominator}


topHeavyExpansionCount = 0
expansionMax = 1000
for expansion in range(1,expansionMax+1):
	fraction = square_two(expansion)
	if len(str(fraction['numerator'])) > len(str(fraction['denominator'])):
		topHeavyExpansionCount += 1
		print(expansion)
		
print(topHeavyExpansionCount)