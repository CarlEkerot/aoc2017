import re


def parse():
    with open('day12.txt') as f:
        return [[int(d) for d in re.findall(r'\d+', l)][1:] for l in f]


def bfs(g, start=0):
    queue = []
    seen = set()
    queue.append(start)
    while len(queue) > 0:
        i = queue.pop()
        seen.add(i)
        [queue.append(n) for n in g[i] if n not in seen]
    return seen


def solve1(g):
    return len(bfs(g))


def solve2(g):
    count = 0
    while any(g):
        start = next(i for i, v in enumerate(g) if v)
        for n in bfs(g, start):
            g[n] = None
        count += 1
    return count


print(solve1(parse()))
print(solve2(parse()))
