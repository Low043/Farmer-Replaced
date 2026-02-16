# Run when get 400 carrots, unlock 8x8 world and restart
# Upgrade everything and unlock mazes and lists
from simple_pumpkin import *
from simple_snake import *

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def handle(x, y):
	if can_harvest():
		harvest()
	
	if y >= 6:
		return plant_carrot()
	if x % 2 != y % 2:
		return plant(Entities.Tree)

clear()
while True:
	force_pumpkin_behavior(simple_snake, handle)
