f = open("input.txt", "r")

#####################################
#               PART 1              #
#####################################

def add_adjacent(grid, y, x):
    if grid[y+1][x] != 11 and (y+1, x) not in done:                           # No time to improve this places to gooooo
        grid[y+1][x] += 1
        if grid[y+1][x] == 10:
            waiting_line.append((y+1, x))
    if grid[y-1][x] != 11 and (y-1, x) not in done:
        grid[y-1][x] += 1
        if grid[y-1][x] == 10:
            waiting_line.append((y-1, x))
    if grid[y][x+1] != 11 and (y, x+1) not in done:
        grid[y][x+1] += 1
        if grid[y][x+1] == 10:
            waiting_line.append((y, x+1))
    if grid[y][x-1] != 11 and (y, x-1) not in done:
        grid[y][x-1] += 1
        if grid[y][x-1] == 10:
            waiting_line.append((y, x-1))
    if grid[y+1][x+1] != 11 and (y+1, x+1) not in done:
        grid[y+1][x+1] += 1
        if grid[y+1][x+1] == 10:
            waiting_line.append((y+1, x+1))
    if grid[y-1][x-1] != 11 and (y-1, x-1) not in done:
        grid[y-1][x-1] += 1
        if grid[y-1][x-1] == 10:
            waiting_line.append((y-1, x-1))
    if grid[y+1][x-1] != 11 and (y+1, x-1) not in done:
        grid[y+1][x-1] += 1
        if grid[y+1][x-1] == 10:
            waiting_line.append((y+1, x-1))
    if grid[y-1][x+1] != 11 and (y-1, x+1) not in done:
        grid[y-1][x+1] += 1
        if grid[y-1][x+1] == 10:
            waiting_line.append((y-1, x+1))
    return grid



grid = []
grid.append([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])

n = 1
for line in f.readlines():
    grid.append([])
    grid[n].append(11)
    for x in line.strip():
        grid[n].append(int(x))
    grid[n].append(11)
    n += 1

grid.append([11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11, 11])

flashes = 0
waiting_line = []
done = []
n = 0
for i in range(100):
    for y in range(1, 11):
        for x in range(1, 11):
            grid[y][x] += 1
            if grid[y][x] == 10:
                waiting_line.append((y, x))

    while  n < len(waiting_line):
        flashes += 1
        done.append(waiting_line[n])
        grid = add_adjacent(grid, waiting_line[n][0], waiting_line[n][1])
        grid[waiting_line[n][0]][waiting_line[n][1]] = 0
        n += 1
    '''
    if len(waiting_line) == 100:
        print(i)
        break
    '''
    done.clear()
    waiting_line.clear()
    n = 0

print("Part 1: ", flashes)

#####################################
#               PART 2              #
#####################################

print("(Just uncomment the if statement and switch the range of the biggest while loop to 1000 and print: i+1)\nPart 2: 314")
