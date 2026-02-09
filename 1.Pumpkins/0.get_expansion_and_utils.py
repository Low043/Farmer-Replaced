# Farm some carrots to run this script.
from snake import *
global failed

def plant_mode(x, y):
	if get_ground_type() != Grounds.Soil:
		till()
	
	plant(Entities.Pumpkin)

def check_mode(x, y):
	global failed
	if not can_harvest():
		plant(Entities.Pumpkin)
		failed = True

clear()
while True:
	snake_sector(plant_mode)
	
	while True:
		failed = False
		snake_sector(check_mode)
		if not failed:
			break

	harvest()