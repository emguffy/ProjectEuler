

cubePermsFound = False
targetPerms = 5
root = 1
cubes = {}
cubeAnswers = []

while cubePermsFound == False:
	print(root)
	cube = root ** 3
	cubeKey = ''.join(sorted(str(cube)))
	if cubeKey in cubes:
		cubes[cubeKey].append(cube)
		if len(cubes[cubeKey]) == targetPerms:
			cubePermsFound = True
			cubeAnswers = cubes[cubeKey]
	else:
		cubes[cubeKey] = [cube]
		
	root += 1
	
print(min(cubeAnswers))
