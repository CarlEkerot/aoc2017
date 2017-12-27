from string import ascii_uppercase

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def parse():
    with open('day19.txt') as f:
        return [list(l[:-1]) for l in f.readlines()]


def find_dir(curr_dir, pos, m):
    alts = [(pos[0] + d[0], pos[1] + d[1]) for d in DIRS]
    if len([p for p in alts if m[p[0]][p[1]] == ' ']) == 3:
        return None

    if m[pos[0]][pos[1]] != '+':
        return curr_dir

    pp = (pos[0] - curr_dir[0], pos[1] - curr_dir[1])
    for d in DIRS:
        np = (pos[0] + d[0], pos[1] + d[1])
        if m[np[0]][np[1]] == ' ' or np == pp:
            continue
        return d


def solve(m):
    pos = (0, m[0].index('|'))
    d = (1, 0)
    s = ''
    num_steps = 1
    while d:
        pos = (pos[0] + d[0], pos[1] + d[1])
        num_steps += 1
        l = m[pos[0]][pos[1]]
        s += l if l in ascii_uppercase else ''
        d = find_dir(d, pos, m)
    return (s, num_steps)


print(solve(parse()))
