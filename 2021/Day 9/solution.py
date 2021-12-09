f = open("input.txt", "r")
f_read = f.readlines()
f.close()

#####################################
#               PART 1              #
#####################################

my_map = []
aux_lst = []
aux2 = []
for x in range(len(f_read[0])+1):
    aux2.append(10)

my_map.append(aux2)

n, m = 0, 0
for line in f_read:
    aux_lst.append(10)
    for num in line.strip():
        aux_lst.append(int(num))
        m += 1
    aux_lst.append(10)
    my_map.append(aux_lst.copy())
    aux_lst.clear()
    m = 0
    n += 1

for x in range(len(f_read[0])-1):
    aux_lst.append(10)

my_map.append(aux2)

risk = 0
lows = []

for y in range(1, len(my_map)-1):
    for x in range(1, len(my_map[0])-1):
        if my_map[y][x] < my_map[y][x+1] and my_map[y][x] < my_map[y][x-1] and my_map[y][x] < my_map[y-1][x] and \
                my_map[y][x] < my_map[y+1][x]:
           risk += my_map[y][x] + 1
           lows.append((y, x))

print("Part 1: ", risk)

#####################################
#               PART 2              #
#####################################

size = 1
sizes = []
check = []
done = []


def adjacent(check, y, x):
    if (y+1, x) not in done and (y+1, x) not in check:
        check.append((y+1, x))
    if (y-1, x) not in done and (y-1, x) not in check:
        check.append((y-1, x))
    if (y, x+1) not in done and (y, x+1) not in check:
        check.append((y, x+1))
    if (y, x-1) not in done and (y, x-1) not in check:
        check.append((y, x-1))
    return check


for y in range(1, len(my_map)-1):
    for x in range(1, len(my_map[0])-1):
        if (y, x) in lows:
            check = []
            done = []
            size = 1
            done.append((y, x))
            check = adjacent(check, y, x)
            while len(check) != 0:
                if my_map[check[0][0]][check[0][1]] == 9 or my_map[check[0][0]][check[0][1]] == 10:
                    done.append(check[0])
                    check.remove(check[0])
                else:
                    size += 1
                    check = adjacent(check, check[0][0], check[0][1])
                    done.append(check[0])
                    check.remove(check[0])
            sizes.append(size)


sizes.sort()
res = sizes[len(sizes)-1] * sizes[len(sizes)-2] * sizes[len(sizes)-3]
print("Part 2: ", res)
