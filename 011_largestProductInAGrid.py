
f = open('LargestProductInAGrid.txt','rU')
stream = f.read()
f.closed

grid = []
row = []
for row in stream.split('\n'):
	gridRow = []
	for item in row.split(): 
		gridRow.append(int(item))
	grid.append(gridRow)

maxProduct = 0
# Check back-slash
for y in range(0,17):
	for x in range (0,17):
		product = grid[y][x] * grid[y+1][x+1] * grid[y+2][x+2] * grid[y+3][x+3]
		if product > maxProduct:
			maxProduct = product

# Check forward-slash
	for y in range(3,20):
		for x in range (0,17):
			product = grid[y][x] * grid[y-1][x+1] * grid[y-2][x+2] * grid[y-3][x+3]
			if product > maxProduct:
				maxProduct = product	

# Check columns
for y in range(0,17):
	for x in range (0,20):
		product = grid[y][x] * grid[y+1][x] * grid[y+2][x] * grid[y+3][x]
		if product > maxProduct:
			maxProduct = product

# Check rows
for y in range(0,20):
	for x in range (0,17):
		product = grid[y][x] * grid[y][x+1] * grid[y][x+2] * grid[y][x+3]
		if product > maxProduct:
			maxProduct = product

print maxProduct