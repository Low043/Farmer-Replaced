global pumpkin_ready

def handle_pumpkin():
	global pumpkin_ready

	if get_ground_type() != Grounds.Soil:
		till()
	
	plant(Entities.Pumpkin)

	if num_items(Items.Fertilizer) > 0:
		use_item(Items.Fertilizer)

	if not can_harvest():
		plant(Entities.Pumpkin)
		pumpkin_ready = False

def pumpkin_wrapper(default_task):
	def wrapper(x, y):
		if x < 6 and y < 6:
			return handle_pumpkin()
		return default_task(x, y)
	return wrapper

def force_pumpkin_behavior(navigation_fn, task):
	global pumpkin_ready
	pumpkin_ready = True

	navigation_fn(pumpkin_wrapper(task))
	if pumpkin_ready:
		harvest()
