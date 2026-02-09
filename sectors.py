LAST_SQUARE = get_world_size() - 1
START = 0
END = 1
X = 0
Y = 1

FULL_SECTOR = ((0, 0), (LAST_SQUARE, LAST_SQUARE))

def sector(x1, y1, x2, y2):
    return ((x1, y1), (x2, y2))

def range_sector_x(sector):
    return range(sector[START][X], sector[END][X] + 1)

def range_sector_y(sector):
    return range(sector[START][Y], sector[END][Y] + 1)

def first_sector_x(sector):
    return sector[START][X]

def last_sector_x(sector):
    return sector[END][X]

def first_sector_y(sector):
    return sector[START][Y]

def last_sector_y(sector):
    return sector[END][Y]

def split_sector(sector_data, parts):
    x1, y1 = sector_data[START]
    x2, y2 = sector_data[END]
    width = x2 - x1 + 1

    actual_parts = parts
    if parts > width:
        actual_parts = width

    part_width = width // actual_parts
    extra_columns = width % actual_parts

    sectors = []
    current_x = x1

    for i in range(actual_parts):
        current_part_width = part_width
        if i < extra_columns:
            current_part_width += 1

        end_x = current_x + current_part_width - 1
        sectors.append(sector(current_x, y1, end_x, y2))

        current_x = end_x + 1

    return sectors

if __name__ == "__main__":
    for sector in split_sector(FULL_SECTOR, 4):
        quick_print(sector)