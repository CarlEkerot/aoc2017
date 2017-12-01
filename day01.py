def parse():
    with open('day01.txt') as f:
        return [int(c) for c in f.read().strip()]


def rotatesum(l, s):
    return sum(x for x, y in zip(l, l[s:] + l[:s]) if x == y)


l = parse()
print(rotatesum(l, 1))
print(rotatesum(l, len(l) // 2))
