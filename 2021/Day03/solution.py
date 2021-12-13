f = open("input.txt", "r")
lines = f.readlines()
f.close()


def bin_dec(lst):
    m, res = 0, 0
    while m < len(lst):
        if lst[m] == "1":
            res = res + 2**(len(lst)-m-1)
        m += 1

    return res


#####################################
#               PART 1              #
#####################################


zero, one = 0, 0
gamma, epsilon = "", ""
n = 0

for i in range(12):
    for lin in lines:
        if lin[i] == "0":
            zero += 1
        else:
            one += 1

    if one > zero:
        epsilon += "1"
        gamma += "0"
    else:
        epsilon += "0"
        gamma += "1"

    one, zero = 0, 0

print("Part 1: ", bin_dec(gamma) * bin_dec(epsilon))


#####################################
#               PART 2              #        A different approach
##################################### 

l_one = []                      
l_zero = []
one, zero = 0, 0
copyl = lines.copy()
i = 0

while len(lines) > 1:
    for lin in lines:
        if lin[i] == "0":
            zero += 1
            l_zero.append(lin)
        else:
            one += 1
            l_one.append(lin)
    if one >= zero:
        lines = l_one
    else:
        lines = l_zero

    i += 1
    one, zero = 0, 0
    l_one = []
    l_zero = []

o2 = bin_dec(lines[0].strip())

lines = copyl
i = 0

while len(lines) > 1:              # Repeat beacause fastttttttttttteeeerrrrrrrrr
    for lin in lines:
        if lin[i] == "0":
            zero += 1
            l_zero.append(lin)
        else:
            one += 1
            l_one.append(lin)
    if one >= zero:
        lines = l_zero
    else:
        lines = l_one

    i += 1
    one, zero = 0, 0
    l_one = []
    l_zero = []

co2 = bin_dec(lines[0].strip())

print("Part 2: ", co2*o2)
