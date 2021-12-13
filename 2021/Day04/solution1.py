fp = open("input.txt", "r")


def unmarked_n(card):
    res = 0
    for y in range(5):
        for x in range(5):
            if card[y][x] != 100:
                res += card[y][x]

    return res

def IsWinner(card):
    for y in card:
        if y.count(100) == 5:
            return True

    n = True
    for x in card:
        n = True
        for y in range(5):
            if x[y] != 100:
                n = False
                break

    return n



def play(card, num):
    if num in card[0] or num in card[1] or num in card[2] or num in card[3] or num in card[4]:
        for y in range(5):
            for x in range(5):
                if card[y][x] == num:
                    card[y][x] = 100
    return


num_calls = [int(x) for x in fp.readline().strip("\n").split(",")]
cards = []

while fp.readline():
    card = []
    for i in range(5):
        card.append([int(x) for x in fp.readline().strip("\n").split(" ") if x != ""])
    cards.append(card)

winners = []
winner = False
x = 0
m = 0

for n in range(100):
    for e in range(100):
        play(cards[e], num_calls[n])
        if IsWinner(cards[e]):
            winner = True
            x = e
            m = num_calls[n]
    if winner == True:
        break


print(m * unmarked_n(cards[x]))
