from itertools import count


def parse():
    with open('day13.txt') as f:
        return [tuple(map(int, l.split(': '))) for l in f]


def state(r, t):
    return (r - 1) - abs(t % (2 * (r - 1)) - (r - 1))


def solve1(layers):
    return sum(d * r for (d, r) in layers if state(r, d) == 0)


def solve2(layers):
    return next(n for n in count()
                if all(state(r, d + n) > 0 for (d, r) in layers))


print(solve1(parse()))
print(solve2(parse()))
