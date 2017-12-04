from itertools import combinations


def parse():
    with open('day02.txt') as f:
        return [[int(n) for n in l.split()] for l in f.readlines()]


def solve1(m):
    return sum(max(r) - min(r) for r in m)


def solve2(m):
    return sum(max(t) // min(t)
               for r in m for t in combinations(r, 2)
               if max(t) % min(t) == 0)


print(solve1(parse()))
print(solve2(parse()))
