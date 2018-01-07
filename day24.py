from collections import defaultdict


def parse():
    with open('day24.txt') as f:
        g = defaultdict(lambda: set())
        for l in f:
            a, b = tuple(map(int, l.strip().split('/')))
            g[a].add(b)
            g[b].add(a)
        return g


def dfs(g, n, p, key):
    cs = [o for o in g[n] if (n, o) not in p and (o, n) not in p]
    if not cs:
        return len(p), sum(a + b for a, b in p)
    return max((dfs(g, o, p + [(n, o)], key) for o in cs), key=key)


def solve(g, key):
    return max(dfs(g, n, [(0, n)], key) for n in g[0])[1]


print(solve(parse(), lambda t: t[1]))
print(solve(parse(), lambda t: t))
