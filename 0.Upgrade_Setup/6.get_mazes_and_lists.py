# Unlock 8x8 world, lists and mazes
# Upgrade fertilizer, trees and pumpkins
from simple_pumpkin import *
from simple_snake import *

def plant_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	plant(Entities.Carrot)

def handle(x, y):
	if can_harvest():
		harvest()
	
	if y >= get_world_size() - 2:
		return plant_carrot()
	if x % 2 != y % 2:
		plant(Entities.Tree)
		if num_items(Items.Fertilizer) > 0:
			use_item(Items.Fertilizer)

clear()
while True:
	force_pumpkin_behavior(simple_snake, handle)
