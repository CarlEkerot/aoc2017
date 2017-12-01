def parse():
    with open('day01.txt') as f:
        return [int(c) for c in f.read().strip()]


def rotatesum(l, step):
    r = l[-step:] + l[:-step]
    return sum(x for (x, y) in zip(l, r) if x == y)


l = parse()
print(rotatesum(l, 1))
print(rotatesum(l, len(l) // 2))
