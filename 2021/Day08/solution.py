f = open("input.txt", "r")

#####################################
#               PART 1              #
#####################################

lines10 = []
lines4 = []
l10 = []
l4 = []

n = 0
for x in f.readlines():
    l10.clear()
    l4.clear()
    for y in x.strip().split(" "):
        if n < 10:
            l10.append(y)
        elif n > 10:
            l4.append(y)
        n += 1
    lines10.append(l10.copy())
    lines4.append(l4.copy())
    n = 0

count = 0
for x in lines4:
    for y in x:
        if len(y) in [2, 4, 3, 7]:
            count += 1

print("Part 1: ", count)

#####################################
#               PART 2              #
#####################################

def cleaner(tabela):
    el = 0
    while el < len(tabela):
        tabela[el] = ""
        el += 1
    return

n = 0
tabela = ["", "", "", "", "", "", ""]
translation = ["", "", "", "", "", "", "", "", "", ""]
res = 0
z = 1000
num = 0

helper = ""
while n < len(lines10):
    for digit in lines10[n]:
        if len(digit) == 2:
            translation[1] = digit
        elif len(digit) == 3:
            translation[7] = digit
        elif len(digit) == 4:
            translation[4] = digit
        elif len(digit) == 7:
            translation[8] = digit

    lines10[n].remove(translation[1])
    lines10[n].remove(translation[4])
    lines10[n].remove(translation[7])
    lines10[n].remove(translation[8])

    for x in translation[7]:
        if x not in translation[1]:
            tabela[0] = x
            helper += x
        else:
            tabela[4] += x
            tabela[5] += x
            helper += x

    for x in translation[4]:
        if x not in translation[7]:
            tabela[1] += x
            tabela[6] += x
            helper += x

    for x in translation[8]:
        if x not in helper:
            tabela[2] += x
            tabela[3] += x

    for digit in lines10[n]:
        if len(digit) == 6 and (tabela[6][0] not in digit or tabela[6][1] not in digit):
            if tabela[6][0] not in digit:
                save = tabela[6][1]
                tabela[6] = tabela[6][0]
                tabela[1] = save
            else:
                save = tabela[6][0]
                tabela[6] = tabela[6][1]
                tabela[1] = save

            translation[0] = digit
            lines10[n].remove(digit)
            break

    for digit in lines10[n]:
        if len(digit) == 6 and (tabela[2][0] not in digit or tabela[2][1] not in digit):
            if tabela[2][0] not in digit:
                save = tabela[2][1]
                tabela[2] = tabela[2][0]
                tabela[3] = save
            else:
                save = tabela[2][0]
                tabela[2] = tabela[2][1]
                tabela[3] = save

            translation[9] = digit
            lines10[n].remove(digit)
            break

    for digit in lines10[n]:
        if len(digit) == 6:
            translation[6] = digit
        elif len(digit) == 5 and tabela[1] in digit:
            translation[5] = digit
        elif tabela[2] in digit:
            translation[2] = digit
        else:
            translation[3] = digit


    for x in lines4[n]:
        for digit in translation:
            if sorted(x) == sorted(digit):
                num = num + translation.index(digit) * z
                z = z // 10

    res = res + num


    cleaner(tabela)
    cleaner(translation)
    helper = ""
    n += 1
    z = 1000
    num = 0

print("Part 2", res)
