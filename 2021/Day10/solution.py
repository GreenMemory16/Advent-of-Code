f = open("input.txt", "r")
lines = [x for x in f.readlines()]
f.close()

#####################################
#               PART 1              #
#####################################

def sum_car(car):
    result = 0
    if car == ")":
        result = 3
    elif car == "]":
        result = 57
    elif car == "}":
        result = 1197
    else:
        result = 25137
    return result

open = ["(", "[", "{", "<"]
close = [")", "]", "}", ">"]

res = 0
waiting_line = []

n = 0
while n < len(lines):
    for car in lines[n]:
        if car in open:
            waiting_line.insert(0, car)
        else:
            if car == close[open.index(waiting_line[0])]:
                waiting_line.pop(0)
            elif car != "\n":
                res = res + sum_car(car)
                break
    n += 1
    waiting_line.clear()

print("Part 1: ", res)

#####################################
#               PART 2              #
#####################################

n = 0
res = 0
final = []
while n < len(lines):
    for car in lines[n]:
        if car in open:
            waiting_line.insert(0, car)
        else:
            if car == close[open.index(waiting_line[0])]:
                waiting_line.pop(0)
            elif car != "\n":
                lines.pop(n)
                n -= 1
                break
            else:
                for x in waiting_line:
                    res = res * 5 + (open.index(x) + 1)
                final.append(res)

    n += 1
    res = 0
    waiting_line.clear()

final = sorted(final)
middle = len(final) // 2

print("Part 2: ", final[middle])
