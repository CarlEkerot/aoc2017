from itertools import product
from day10 import solve2 as knot


def grid(data):
    return ['{0:0128b}'.format(int(knot('%s-%d' % (data, i)), 16))
            for i in range(128)]


def solve1(g):
    return sum(r.count('1') for r in g)


def surrounding(y, x, g):
    s = len(g)
    valid = lambda t: 0 <= t[0] < s and 0 <= t[1] < s and g[t[0]][t[1]] == '1'
    return filter(valid, [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)])


def solve2(g):
    seen = set()
    count = 0
    for y, x in product(range(128), repeat=2):
        if (y, x) in seen or g[y][x] == '0':
            continue

        queue = [(y, x)]
        while queue:
            yp, xp = queue.pop()
            seen.add((yp, xp))
            queue += [s for s in surrounding(yp, xp, g) if s not in seen]
        count += 1
    return count


print(solve1(grid('stpzcrnm')))
print(solve2(grid('stpzcrnm')))
