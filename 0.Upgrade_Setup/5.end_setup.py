# Run until reach Max Speed, World 6x6, Grass 800%, Carrots 400%, Trees 400%
# Also unlock hats, print, water, fertilizer, vars, functions, imports and lists

clear()
while True:
	for y in range(get_world_size()):
		for x in range(get_world_size()):
			if can_harvest():
				harvest()

			if x % 2 != y % 2:
				plant(Entities.Tree)
			elif y >= get_world_size() / 2:
				if get_ground_type() != Grounds.Soil:
					till()
				plant(Entities.Carrot)

			move(East)
		move(North)