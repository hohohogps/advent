from itertools import product

EMPTY = '.'
WALL = '#'
BOX = 'O'
ROBOT = '@'
BIG_BOX_LEFT = '['
BIG_BOX_RIGHT = ']'

EXPANDED_EMPTY = [EMPTY, EMPTY]
EXPANDED_WALL = [WALL, WALL]
EXPANDED_BOX = [BIG_BOX_LEFT, BIG_BOX_RIGHT]
EXPANDED_ROBOT = [ROBOT, EMPTY]

EXPANSIONS = {
    EMPTY: EXPANDED_EMPTY,
    WALL: EXPANDED_WALL,
    BOX: EXPANDED_BOX,
    ROBOT: EXPANDED_ROBOT
}

def read_input(file):
    with open(file, 'r') as f:
        grid = []
        while (line := f.readline()) and line != '\n':
            grid.append(list(line.strip()))

        instructions = ''.join(f.read().splitlines())

        expanded_grid = [
            [symbol for expanded_value in row for symbol in EXPANSIONS.get(expanded_value, [expanded_value])]
            for row in grid
        ]

        return grid, expanded_grid, instructions

def get_start_pos(grid):
    rows, cols = len(grid), len(grid[0])
    for x,y in product(range(rows), range(cols)):
        if grid[x][y] == ROBOT:
            return (x,y)

def print_grid(grid):
    rows, cols = len(grid), len(grid[0])
    for x,y in product(range(rows), range(cols)):
        print(grid[x][y], end= '')
        if y == cols -1:
            print()

def convert_symbols_to_directions(symbols):
    direction_map = {
    '<': (0, -1),  # Left (move left on x-axis)
    '>': (0, 1),   # Right (move right on x-axis)
    '^': (-1, 0),  # Up (move up on y-axis)
    'v': (1, 0)    # Down (move down on y-axis)
    }

    return [direction_map[symbol] for symbol in symbols]

 
def move_object(start_pos, dir, grid):
    x, y = start_pos[0], start_pos[1]
    targetx, targety = x + dir[0], y + dir[1]
    obj = grid[x][y]
    swap = False
    if grid[targetx][targety] == WALL:
        return False

    elif grid[targetx][targety] == EMPTY:
        pass

    elif not move_object((targetx, targety), dir, grid):
        return False

    grid[targetx][targety] = obj
    grid[x][y] = EMPTY
    return True

def move_object_on_expanded_grid(start_pos, dir, grid, swap=True, check = True):
    x, y = start_pos[0], start_pos[1]
    targetx, targety = x + dir[0], y + dir[1]
    obj = grid[x][y]
    if grid[targetx][targety] == WALL:
        return False
    elif grid[targetx][targety] == EMPTY:
        if swap:
            grid[targetx][targety] = obj
            grid[x][y] = EMPTY
        return True
    elif grid[targetx][targety] in (BIG_BOX_LEFT, BIG_BOX_RIGHT):         
        if grid[targetx][targety] == BIG_BOX_LEFT:
            matching_x, matching_y = targetx, targety + 1 
        else:
            matching_x, matching_y = targetx, targety - 1

        if dir in ((1,0), (-1,0)):
            if check and not move_object_on_expanded_grid((matching_x, matching_y), dir, grid, False):
                return False

            if check and not move_object_on_expanded_grid((targetx, targety), dir, grid, False):
                return False

            if swap:
                move_object_on_expanded_grid((matching_x, matching_y), dir, grid, True, False)
        
        if swap:
            moved = move_object_on_expanded_grid((targetx, targety), dir, grid)
            if moved:
                grid[targetx][targety] = obj
                grid[x][y] = EMPTY
                return True
            else:
                return False            

        return True 
    
    return False

def compute_score(grid, part2=False):
    rows, cols = len(grid), len(grid[0])
    check = BOX
    if part2:
        check = BIG_BOX_LEFT
    return sum([x*100+y for x,y in product(range(rows), range(cols)) if grid[x][y] == check])

grid, expanded_grid, instructions = read_input('data15.txt')
robot_pos = get_start_pos(grid)
dirs = convert_symbols_to_directions(instructions)

i = 0
for dir in dirs:
    if move_object(robot_pos, dir, grid):
        robot_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])
    
print('solution 1', compute_score(grid))

robot_pos = get_start_pos(expanded_grid)

for dir in dirs:
    if move_object_on_expanded_grid(robot_pos, dir, expanded_grid):
        robot_pos = (robot_pos[0] + dir[0], robot_pos[1] + dir[1])


print('solution 2', compute_score(expanded_grid, True))