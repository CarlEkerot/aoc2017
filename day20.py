import re
from collections import Counter


def parse():
    with open('day20.txt') as f:
        for l in f:
            pva = re.match(r'p=<(.*)>, v=<(.*)>, a=<(.*)>', l).groups()
            yield list(map(lambda s: tuple(map(int, s.split(','))), pva))


def step(p):
    pos, vel, acc = p
    vel = (vel[0] + acc[0], vel[1] + acc[1], vel[2] + acc[2])
    pos = (pos[0] + vel[0], pos[1] + vel[1], pos[2] + vel[2])
    return pos, vel, acc


def solve1(points, steps=1000):
    for _ in range(steps):
        points = map(step, points)
    return min(enumerate(points), key=lambda p: sum(map(abs, p[1][0])))[0]


def solve2(points, steps=1000):
    for _ in range(steps):
        counts = Counter(p[0] for p in points)
        points = [step(p) for p in points if counts[p[0]] == 1]
    return len(points)


print(solve1(parse()))
print(solve2(list(parse())))
