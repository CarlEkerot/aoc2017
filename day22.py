turn = {
    (0, -1): (1, 0),
    (1, 0): (0, 1),
    (0, 1): (-1, 0),
    (-1, 0): (0, -1),
}


def parse():
    with open('day22.txt') as f:
        return {(x, y): 'I' for y, l in enumerate(f)
                for x, c in enumerate(l) if c == '#'}


def solve(state, steps, evolve=False):
    p = (12, 12)
    d = (0, -1)
    infected = 0
    for i in range(steps):
        if p not in state or state[p] == 'C':
            d = turn[turn[turn[d]]]
            state[p] = 'W' if evolve else 'I'
        elif state[p] == 'W':
            state[p] = 'I'
        elif state[p] == 'I':
            d = turn[d]
            state[p] = 'F' if evolve else 'C'
        elif state[p] == 'F':
            d = (-d[0], -d[1])
            state[p] = 'C'
        infected += 1 if p in state and state[p] == 'I' else 0
        p = (p[0] + d[0], p[1] + d[1])
    return infected


print(solve(parse(), 10000))
print(solve(parse(), 10000000, evolve=True))
