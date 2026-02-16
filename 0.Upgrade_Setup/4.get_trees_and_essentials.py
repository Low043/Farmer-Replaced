# Run until unlock trees (replace bushes), vars, functions and imports

clear()
while True:
	for y in range(3):
		for x in range(3):
			if can_harvest():
				harvest()
			
			if x % 3 == 0:
				# plant(Entities.Tree)
				plant(Entities.Bush)				
			elif x % 3 == 1:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)

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
			
			if x % 3 == 2:
				# plant(Entities.Tree)
				plant(Entities.Bush)
			elif x % 3 == 1:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)

			if x == 2:
				pass
			elif 3 % 2 == 0:
				if y % 2 == 0:
					move(East)
				else:
					move(West)
			else:
				if y % 2 == 0:
					move(West)
				else:
					move(East)
		if y < 2:
			move(South)