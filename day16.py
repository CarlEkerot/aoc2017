def parse():
    with open('day16.txt') as f:
        return f.read().strip().split(',')


def solve1(movs, ps=list('abcdefghijklmnop')):
    l = len(ps)
    for m in movs:
        if m[0] == 's':
            n = int(m[1:])
            ps = ps[l - n:] + ps[:l - n]
        elif m[0] == 'x':
            i, j = tuple(map(int, m[1:].split('/')))
            ps[i], ps[j] = ps[j], ps[i]
        elif m[0] == 'p':
            a, b = m[1:].split('/')
            i, j = ps.index(a), ps.index(b)
            ps[i], ps[j] = ps[j], ps[i]
    return ps


def solve2(movs, ps=list('abcdefghijklmnop'), rounds=10**9):
    states = set()
    i = 0
    while i < rounds:
        ps = solve1(movs, ps)
        ps_str = ''.join(ps)
        if ps_str in states:
            i = (rounds // i) * i
        states.add(ps_str)
        i += 1
    return ps


print(''.join(solve1(parse())))
print(''.join(solve2(parse())))
