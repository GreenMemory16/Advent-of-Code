f = open("input.txt", "r")

#####################################
#               PART 1              #
#####################################


def part_one(coms):
    horizontal, depth = 0, 0
    for command in coms:
        x = command.split(" ")
        if x[0] == "forward":
            horizontal += int(x[1])
        elif x[0] == "down":
            depth += int(x[1])
        else:
            depth -= int(x[1])

    return horizontal*depth


commands = f.readlines()
f.close()

print("Part 1: ", part_one(commands))

#####################################
#               PART 2              #
#####################################


def part_two(coms):
    horizontal, depth, aim = 0, 0, 0

    for command in coms:
        x = command.split(" ")
        if x[0] == "forward":
            horizontal += int(x[1])
            depth += int(x[1])*aim
        elif x[0] == "down":
            aim += int(x[1])
        else:
            aim -= int(x[1])

    return horizontal*depth


print("Part 2: ", part_two(commands))
