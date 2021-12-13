f = open("input.txt", "r")
fishes = {}
for i in range(9):
    fishes[i] = 0

starting_fish = [int(x) for x in f.readline().split(",")]
for i in starting_fish:
    fishes[i] += 1

f.close()
    
#####################################
#               PART 1              #
#####################################


def start_simulation(days, fishes):

    for i in range(days):
        fishes = simulate_day(fishes)
    return fishes


def simulate_day(fishes):
    n = 8
    save = 0
    save2 = fishes[8]

    while n >= 0:
        save2 = save
        save = fishes[n]
        fishes[n] = save2

        if n == 0:
            fishes[6] = fishes[6] + save
            fishes[8] = save
        n = n - 1

    return fishes


def counter(fishes):
    count = 0
    for i in range(9):
        count = count + fishes[i]

    return count


fishes = start_simulation(80, fishes)

print("Part 1: ", counter(fishes))


#####################################
#               PART 2              #
#####################################

fishes = start_simulation(176, fishes)

print("Part 2: ", counter(fishes))
