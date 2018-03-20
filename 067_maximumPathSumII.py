
with open("MaximumPathSumII.txt","r") as f:
	triangle = []
	numberOfRows = 0
	for line in f:
		row = line.split()
		
		int_row = []
		for item in row:
			int_row.append(int(item))
			
		triangle.append(int_row)
		numberOfRows += 1

	print "row " + str(len(triangle)-1) + ": " + str(triangle[len(triangle)-1])
		
	for row in reversed(range(0,len(triangle)-1)):
		print "row " + str(row) + ": " + str(triangle[row])
		for columnIndex in range(0,len(triangle[row])):
			maxFork = 0
			for fork in range(columnIndex,columnIndex+2):
				candidate = triangle[row + 1][fork]
				if candidate > maxFork:
					maxFork = candidate
			
			triangle[row][columnIndex] += maxFork
		
		print "row " + str(row) + ": " + str(triangle[row])
			
	print triangle[0][0]