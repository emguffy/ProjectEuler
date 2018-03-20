import math 

rows = 2
columns = 2

def numberOfRoutes(r,c):
	numerator = math.factorial(r+c)
	denominator = math.factorial(r) * math.factorial(c)
	return numerator / denominator
	
print numberOfRoutes(20,20)
	