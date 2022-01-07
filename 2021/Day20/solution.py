import copy

f = open("input.txt", "r")

translation = [x for x in f.readline().strip()]

floor = []
inicial_values = []

f.readline()

square = 300
for x in range(square):
    floor.append([])
    for y in range(square):
        floor[x].append(".")

square2 = 100
for x in range(square2):
    a = [y for y in f.readline().strip()]
    inicial_values.append(a)

middle_try = 100
for x in range(middle_try, middle_try + square2):
    for y in range(middle_try, middle_try + square2):
        floor[x][y] = inicial_values[x-middle_try][y-middle_try]


def matrix_printer(lst):
    for x in range(len(lst)):
        for y in range(len(lst)):
            print(lst[x][y], end="")
        print()


def floor_cleaner(lst):
    len_lst = len(lst)

    for y in range(len_lst):
        lst[0][y] = "."
        lst[1][y] = "."
        lst[2][y] = "."
        lst[299][y] = "."
        lst[298][y] = "."
        lst[297][y] = "."


    for x in range(len_lst):
        lst[x][0] = "."
        lst[x][1] = "."
        lst[x][2] = "."
        lst[x][299] = "."
        lst[x][298] = "."
        lst[x][297] = "."



floor_holder = copy.deepcopy(floor)

def one_cycle():
    square = 300
    for y in range(square):
        for x in range(square):
            line = ""
            if y == 20 and x == 20:
                print("yey")
            for vector in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,0), (0,1), (1,-1), (1,0), (1,1)]:
                if square-1 >= x + vector[0] and x + vector[0] >= 0 and square-1 >= y + vector[1] and y + vector[1] >= 0:
                    line += floor[x+vector[0]][y+vector[1]]
                else:
                    line += "."
            binnary = ""
            for n in line:
                if n == ".":
                    binnary += "0"
                else:
                    binnary += "1"

            floor_holder[x][y] = int(binnary, 2)


for i in range(2):
    one_cycle()
    floor_size = len(floor_holder)
    for x in range(floor_size):
        for y in range(floor_size):
            floor[x][y] = translation[floor_holder[x][y]]
    if i % 2 == 1:
        floor_cleaner(floor)

count = 0
for x in range(len(floor)):
    for y in range(len(floor)):
        if floor[x][y] == "#":
            count += 1

matrix_printer(floor)
print(count)
