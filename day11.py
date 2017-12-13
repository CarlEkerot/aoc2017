from operator import add
from itertools import accumulate

# http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
movements = {
    'n':  (1, 0, -1),
    'ne': (1, -1, 0),
    'se': (0, -1, 1),
    's':  (-1, 0, 1),
    'sw': (-1, 1, 0),
    'nw': (0, 1, -1),
}


def parse():
    with open('day11.txt') as f:
        return map(movements.get, f.read().strip().split(','))


def dists(m):
    return accumulate(m, lambda a, b: tuple(map(add, a, b)))


def solve1(m):
    return max(list(dists(m))[-1])


def solve2(m):
    return max(map(max, dists(m)))


print(solve1(parse()))
print(solve2(parse()))
