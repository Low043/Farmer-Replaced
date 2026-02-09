clear()
while True:
	for i in range(3):
		if can_harvest():
			harvest()
		
		if i % 2 == 0:
			plant(Entities.Bush)

		move(East)
	move(North)