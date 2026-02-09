# Enable delegating tasks to other drones
MEGAFARM_UNLOCKED = False
summoned_drones = []

def delegate(task):
	if not MEGAFARM_UNLOCKED:
		return False
	
	drone_id = spawn_drone(task)
	if not drone_id:
		return False

	summoned_drones.append(drone_id)
	return True

def get_drones():
	return summoned_drones

def clear_drones():
	summoned_drones = []

def wait_for_drones():
	for drone_id in summoned_drones:
		wait_for(drone_id)
	clear_drones()
