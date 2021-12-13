#######################################################
# To get the first solution, get rid of the for loop  #
# and make it read only the first folding instruction #
#######################################################

f = open("input.txt", "r")

instructions = []
folds = []

for n in range(840):
    instructions.append(f.readline().strip().split(","))

for n in range(13):
    folds.append(f.readline()[11:].strip())
    folds[n] = folds[n].split("=")
folds.pop(0)

biggest_x = 0
biggest_y = 0
for cor in instructions:
    if int(cor[0]) > biggest_x:
        biggest_x = int(cor[0])
    if int(cor[1]) > biggest_y:
        biggest_y = int(cor[1])
biggest_y += 3
guide = []

for n in range(biggest_x+1):
    guide.append([])
    for m in range(biggest_y+1):
        guide[n].append(".")

for cor in instructions:
    guide[int(cor[0])][int(cor[1])] = "#"


def y_fold(y):
    for vertical in guide:
        helping_lst.append(vertical[y+1:])


def y_cut(y):
    for vertical in guide:
        del vertical[y:]


def y_overlap():
    for x in range(len(guide)):
        for y in range(len(guide[0])):
            if helping_lst[x][y] == "#":
                guide[x][y] = "#"


def x_fold(x):
    for horizontal in range(x+1, len(guide)):
        helping_lst.append(guide[horizontal])


def x_cut(x):
    del guide[x:]


def x_overlap():
    for x in range(len(guide)):
        for y in range(len(guide[0])):
            if helping_lst[x][y] == "#":
                guide[x][y] = "#"


helping_lst = []
for instruc in folds:
    if instruc[0] == "y":
        y_fold(int(instruc[1]))
        y_cut(int(instruc[1]))
        for i in helping_lst:
            i.reverse()
        y_overlap()
        helping_lst.clear()
    else:
        x_fold(int(instruc[1]))
        x_cut(int(instruc[1]))
        helping_lst.reverse()
        x_overlap()
        helping_lst.clear()

count = 0
for x in range(len(guide)):
    for y in range(len(guide[0])):
        if guide[x][y] == "#":
            count += 1

print(len(guide))

for m in range(len(guide[0])):
    for n in range(len(guide)):
        print(guide[n][m], end="")
    print("")
