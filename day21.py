import re
from itertools import product


def rot(p):
    l = [2, 0, 3, 1] if len(p) == 4 else [6, 3, 0, 7, 4, 1, 8, 5, 2]
    return ''.join(p[i] for i in l)


def flip(p):
    l = [1, 0, 3, 2] if len(p) == 4 else [2, 1, 0, 5, 4, 3, 8, 7, 6]
    return ''.join(p[i] for i in l)


def parse():
    with open('day21.txt') as f:
        rules = {}
        for l in f:
            k, v = map(lambda s: s.replace('/', ''),
                       re.match(r'(.*) => (.*)', l).groups())
            for t in [rot, rot, rot, rot, flip, rot, rot, rot]:
                k = t(k)
                rules[k] = v
        return rules


def square_indices(x, y, pixels, width):
    return [y * pixels**2 * width + b * pixels*width + x * pixels + a
            for b, a in product(range(pixels), repeat=2)]


def get_squares(grid):
    pixels = 3 if len(grid) % 2 else 2
    width = int((len(grid) / pixels**2)**0.5)
    return [''.join(grid[i] for i in square_indices(x, y, pixels, width))
            for y, x in product(range(width), repeat=2)]


def merge(squares):
    width = int(len(squares)**0.5)
    pixels = int(len(squares[0])**0.5)
    new_grid = [0] * len(squares) * len(squares[0])
    for y, x in product(range(width), repeat=2):
        square = squares[width * y + x]
        indices = square_indices(x, y, pixels, width)
        for i, v in zip(indices, square):
            new_grid[i] = v
    return ''.join(new_grid)


def solve(rules):
    grid = '.#...####'
    for i in range(1, 19):
        grid = merge([rules[s] for s in get_squares(grid)])
        print(i, grid.count('#'))


solve(parse())
