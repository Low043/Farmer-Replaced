clear()
while True:
	# y == 1
	if can_harvest():
		harvest()

	plant(Entities.Bush)

	move(North)
	
	# y == 2
	if can_harvest():
		harvest()

	move(North)
	
	# y == 3
	if can_harvest():
		harvest()

	plant(Entities.Bush)

	move(North)