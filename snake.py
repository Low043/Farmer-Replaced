from sectors import *

def snake_direction(y):
    if y % 2 == 0:
        return East
    return West

def snake_real_x(i, dir, sector):
    if dir == West:
        return last_sector_x(sector) - i
    return i

def snake_sector(task, sector = FULL_SECTOR):
    for y in range_sector_y(sector):
        dir = snake_direction(y)

        for i in range_sector_x(sector):
            x = snake_real_x(i, dir, sector)
            task(x, y)
            if i != last_sector_x(sector):
                move(dir)
        
        move(North)

if __name__ == "__main__":
    clear()
    snake_sector(quick_print, FULL_SECTOR)
