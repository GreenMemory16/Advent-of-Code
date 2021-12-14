f = open("input.txt", "r")

#####################################
#               PART 1              #
#####################################

inicial = [x for x in f.readline().strip()]
rules = {}
f.readline()
first_letter = inicial[0]
last_letter = inicial[-1]

fake_inicial = inicial.copy()

for line in f.readlines():
    key, value = line.strip().split(" -> ")
    rules[key] = value

n = 0
for m in range(10):
    while n < len(inicial)-1:
        pair = inicial[n] + inicial[n+1]
        letter = rules[pair]
        inicial.insert(n+1, letter)
        n += 2
    n = 0

results = {}
for x in inicial:
    if x not in results:
        results[x] = 1
    else:
        results[x] += 1

biggest = 0
smallest = 100000000

for key in results:
    if results[key] > biggest:
        biggest = results[key]
    if results[key] < smallest:
        smallest = results[key]

print("Part 1: ", biggest-smallest)

#####################################
#               PART 2              #
#####################################

pairs = {}
pair_counter = {}

for x in rules:
    pair_counter[x] = 0

for x in range(len(fake_inicial)-1):
    pair_counter[fake_inicial[x] + fake_inicial[x+1]] += 1

helper = []
counter_helper = pair_counter.copy()
n = 0
for x in range(40):
    helper = [x for x in pair_counter if pair_counter[x] != 0]
    for y in helper:
        pair_counter[y] -= counter_helper[y]
        pair_counter[y[0] + rules[y]] += counter_helper[y]
        pair_counter[rules[y] + y[1]] += counter_helper[y]
    counter_helper = pair_counter.copy()

results = {}
for x in range(65, 91):
    results[chr(x)] = 0

for x in pair_counter:
    results[x[0]] += pair_counter[x]
    results[x[1]] += pair_counter[x]

results[first_letter] += 1    #First and Last letters
results[last_letter] += 1

biggest = 0
smallest = 10000000000000000
for x in results:
    if results[x] > biggest:
        biggest = results[x]
    if results[x] < smallest and results[x] != 0:
        smallest = results[x]

print("Part 2: ", (biggest // 2) - (smallest // 2))
