f = open("input.txt", "r")

#####################################
#               PART 1              #
#####################################

scan = []
for line in f.readlines():
    x = line.strip().split("-")
    scan.append(x)

tunnels = {}

for line in scan:
    if line[0] not in tunnels:
        tunnels[line[0]] = []
    tunnels[line[0]].append(line[1])
    if line[1] not in tunnels:
        tunnels[line[1]] = []
    tunnels[line[1]].append(line[0])

path = []
paths = []

def recursion():
    global count
    if path[-1] == "end":
        count += 1
        return paths.append(path.copy())
    else:
        for x in tunnels[path[-1]]:
            if (x == x.upper()) or (x not in path):
                path.append(x)
                recursion()
                path.pop()


count = 0
path.append("start")
recursion()
print("Part 1: ", len(paths))
print(count)

#####################################
#               PART 2              #
#####################################

def recursion2(special):                             # This takes a minute to run....
    if path[-1] == "end":
        return paths.append(path.copy())
    else:
        for x in tunnels[path[-1]]:
            if (x != "start") and ((x == x.upper()) or (x not in path) or (x == special and path.count(special) < 2)):
                path.append(x)
                recursion2(special)
                path.pop()

path.clear()
path.append("start")
paths.clear()
count = 0

small = []
for x in tunnels:
    if x == x.lower() and x != "start" and x != "end":
        small.append(x)

for x in small:
    recursion2(x)

paths2 = []

for i in range(len(paths)):
    if paths[i] not in paths2:
        paths2.append(paths[i])

print(len(paths2))
