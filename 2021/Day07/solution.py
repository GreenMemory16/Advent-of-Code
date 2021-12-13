f = open("input.txt", "r")

#####################################
#               PART 1              #
#####################################

pos_inicial = [int(x) for x in f.readline().split(",")]
save = pos_inicial.copy()
f.close()

biggest = 0
for pos in pos_inicial:
    if pos > biggest:
        biggest = pos

fuel, n = 0, 0
smallest = 1000000000
fuel_lst = []
while n < biggest + 1:
    for pos in save:
        fuel = fuel + abs(pos - n)
    n += 1
    if fuel < smallest:
        smallest = fuel
    fuel = 0

print("Part 1: ", smallest)

#####################################
#               PART 2              #
#####################################

def sum_n(x):
    return x * (x-1) // 2

n, smallest = 0, 1000000000000

while n < biggest + 1:
    for pos in save:
        x = abs(pos - n)
        fuel += sum_n(x+1)
    n += 1
    if fuel < smallest:
        smallest = fuel
    fuel = 0

print("Part 2: ", smallest)
