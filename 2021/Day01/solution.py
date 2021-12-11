fp = open("input.txt", "r")
lines = [int(x) for x in fp.readlines()]

#####################################
#               PART 1              #
#####################################

previous = 0
count = -1

for line in lines:
    if line > previous:
        count += 1
    previous = line

print("Part 1: ", count)

#####################################
#               PART 2              #
#####################################

n = 3
soma1, soma2, count = 0, 0, 0

while n < len(lines):
    soma1 = lines[n-1] + lines[n-2] + lines[n-3]
    soma2 = lines[n] + lines[n-1] + lines[n-2]

    if soma2 > soma1:
        count += 1

    soma1, soma2 = 0, 0
    n = n + 1

print("Part 2: ", count)
