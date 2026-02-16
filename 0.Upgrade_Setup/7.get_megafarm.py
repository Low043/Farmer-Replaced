# Farm some weird substance before running this script
directions = [North, East, South, West]

# Maze summoning
def get_summon_item_qtd(maze_size):
	lvl = num_unlocked(Unlocks.Mazes)
	formula = 2 ** (lvl - 1)
	return maze_size * formula
	
def summon_maze(maze_size):
	qtd = get_summon_item_qtd(maze_size)
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, qtd)

# Movement checking
def check_forward(dir_index):
	return can_move(directions[dir_index]), dir_index
	
def check_backward(dir_index):
	dir_index = (dir_index + 2) % 4
	return can_move(directions[dir_index]), dir_index

def check_right(dir_index):
	dir_index = (dir_index + 1) % 4
	return can_move(directions[dir_index]), dir_index
	
def check_left(dir_index):
	dir_index = (dir_index - 1) % 4
	return can_move(directions[dir_index]), dir_index

# Logic
def choose_path(dir_index):
	check_paths = [
		check_right, check_forward,
		check_left, check_backward
	]

	chosen_path = None
	for check_path in check_paths:
		allowed_path, index = check_path(dir_index)
		if not allowed_path:
			continue
		if chosen_path == None:
			chosen_path = index
			break

	return chosen_path

def find_treasure(dir_index = 0, start_moving = False):
	if start_moving:
		move(directions[dir_index])

	while True:
		treasure = measure()
		if treasure == None:
			break
	
		x = get_pos_x()
		y = get_pos_y()
		
		if x == treasure[0] and y == treasure[1]:
			return harvest()
		
		dir_index = choose_path(dir_index)
		if dir_index == None:
			break
		move(directions[dir_index])

if __name__ == '__main__':
	clear()
	while True:
		summon_maze(get_world_size())
		find_treasure()