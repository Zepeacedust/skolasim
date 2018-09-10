import random
import math
for x in range(6):
	currentstat = [random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)]
	currentstat.sort()
	currentstat.pop(1)
	output = [sum(currentstat), (math.floor((sum(currentstat)-10)/2))]
	print(output)
input("done.")