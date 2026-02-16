# Run until reach MAX speed, 6x6 world and unlock fertilizer
# Grass: 800%, Carrots: 400%, Trees: 400%, Pumpkins: 200%
from simple_snake import *

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def handle(x, y):
	if can_harvest():
		harvest()
	
	if y >= ROW_LENGTH // 2:
		return plant_carrot()
	if x % 2 != y % 2:
		return plant(Entities.Tree)

clear()
while True:
	simple_snake(handle)
