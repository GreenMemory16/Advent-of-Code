import heapq

###########################################################
# This was more of a learning puzzle, as I had never used #
# any library nor I knew about the dijkstra algorithm, so #
# this code is not fully original                         #
###########################################################

f = open("input.txt", "r")

cave = []
empty_c = []
for x in range(100):
    cave.append([])

n = 0
for line in f.readlines():
    for num in line.strip():
        cave[n].append(int(num))
        n += 1
    n = 0

len_x = len(cave)
len_y = len(cave[0])
cost = {}
pos = [(0, 0, 0)]
heapq.heapify(pos)
done = set()

while len(pos) > 0:
    c, x, y = heapq.heappop(pos)

    if (x, y) in done:
        continue

    done.add((x, y))

    cost[(x, y)] = c

    if x == len_x - 1 and y == len_y - 1:
        break

    for a, b in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        one = x + a
        two = y + b
        if not (0 <= one < len_x and 0 <= two < len_y):
            continue
        heapq.heappush(pos, (c + cave[one][two], one, two))

print("Part 1: ", cost[(len_x - 1, len_y - 1)])
