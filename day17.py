def solve1(steps, rounds=2017):
    buf = [0]
    pos = 0
    for i in range(1, rounds + 1):
        pos = (pos + steps) % i + 1
        buf.insert(pos, i)
    return buf[buf.index(rounds) + 1]


def solve2(steps, rounds=50000000):
    pos = 0
    last_zero = None
    for i in range(1, rounds + 1):
        pos = (pos + steps) % i + 1
        if pos == 1:
            last_zero = i
    return last_zero


print(solve1(377))
print(solve2(377))
