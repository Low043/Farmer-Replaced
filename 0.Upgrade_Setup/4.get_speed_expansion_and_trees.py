clear()
while True:
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if can_harvest():
				harvest()
			
			if x % 3 == 0:
				plant(Entities.Bush)
			elif x % 3 == 1:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)

			move(East)
		move(North)