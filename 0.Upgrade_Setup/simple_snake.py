ROW_LENGTH = get_world_size()
ROW_LAST_INDEX = ROW_LENGTH - 1
WORLD_AREA = ROW_LENGTH ** 2
WORLD_LAST_INDEX = WORLD_AREA - 1
reversed = False

def reverse():
    global reversed
    reversed = not reversed

def get_pos(index):
    if reversed:
        index = WORLD_LAST_INDEX - index
    
    x = index % ROW_LENGTH
    y = index // ROW_LENGTH
    
    if y % 2 == 1:
        x = ROW_LAST_INDEX - x
        
    return x, y

def _move(current_x, current_y, next_index):
    if next_index > WORLD_LAST_INDEX:
        return

    next_x, next_y = get_pos(next_index)
    if next_x > current_x:
        return move(East)
    if next_x < current_x:
        return move(West)
    if next_y > current_y:
        return move(North)
    return move(South)

def simple_snake(task):
    for i in range(WORLD_AREA):
        x, y = get_pos(i)
        task(x, y)
        _move(x, y, i + 1)
    reverse()