fp = open("input.txt", "r")
sea = []

linhas = fp.readlines()

fp.close()

def create_vertical_line(sea, a, b, y):
    if b > a:
        for i in range(a, b+1):
            sea[i][y] = sea[i][y] + 1
    else:
        for i in range(b, a+1):
            sea[i][y] = sea[i][y] + 1

    return sea


def create_horizontal_line(sea, a, b, x):
    if b > a:
        for i in range(a, b+1):
            sea[x][i] = sea[x][i] + 1
    else:
        for i in range(b, a+1):
            sea[x][i] = sea[x][i] + 1

    return sea


def create_diagonal_lines(sea, x1, x2, y1, y2):
    if x2 > x1 and y2 > y1:
        for i in range(x1, x2+1):
            sea[y1][i] = sea[y1][i] + 1
            y1 = y1 + 1
    elif x2 > x1 and y1 > y2:
        for i in range(x1, x2+1):
            sea[y1][i] = sea[y1][i] + 1
            y1 = y1 - 1
    elif x1 > x2 and y2 > y1:
        for i in range(x2, x1+1):
            sea[y2][i] = sea[y2][i] + 1
            y2 = y2 - 1
    elif x1 > x2 and y1 > y2:
        for i in range(x2, x1+1):
            sea[y2][i] = sea[y2][i] + 1
            y2 = y2 + 1

    return sea


#####################################
#               PART 1              #
#####################################

def part_one_two(linhas, size, sea, part):
    for i in range(size):
        sea.append(0)
    for i in range(size):
        sea[i] = [0 for x in range(size)]

    for line in linhas:
        l = line.split(" -> ")
        one = l[0]
        two = l[1]
        x1, y1 = one.split(",")
        x2, y2 = two.split(",")
        x1 = int(x1)
        y1 = int(y1)
        x2 = int(x2)
        y2 = int(y2)

        if x1 == x2:
            sea = create_vertical_line(sea, y1, y2, x1)
        elif y1 == y2:
            sea = create_horizontal_line(sea, x1, x2, y1)
        else:
            if part == 2:
                sea = create_diagonal_lines(sea, x1, x2, y1, y2)

    count = 0
    for i in sea:
        for j in i:
            if j >= 2:
                count += 1

    return count

print("Part 1: ", part_one_two(linhas, 1000, sea, 1))


#####################################
#               PART 2              #
#####################################
sea = []

print("Part 2: ", part_one_two(linhas, 1000, sea, 2))
