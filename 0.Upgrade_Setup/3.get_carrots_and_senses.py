clear()
while True:
	for y in range(3):
		for x in range(3):
			if can_harvest():
				harvest()
			
			if x % 2 == y % 2:
				plant(Entities.Bush)
			
			if x == 2:
				pass
			elif y % 2 == 0:
				move(East)
			else:
				move(West)
		if y < 2:
			move(North)
	
	for y in range(3):
		for x in range(3):
			if can_harvest():
				harvest()
			
			if x % 2 == y % 2:
				plant(Entities.Bush)
			
			if x == 2:
				pass
			elif y % 2 == 0:
				move(West)
			else:
				move(East)
		if y < 2:
			move(South)