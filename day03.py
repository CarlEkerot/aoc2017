def solve1(size):
    max_square = int((size - 1)**0.5) + 1
    spiral = [0]
    for s in range(3, max_square + 2, 2):
        circum = s**2 - (s - 2)**2
        n = s - 1
        elems = [abs((x % n) - n // 2) + n // 2 for x in range(circum)]
        spiral += elems[1:]
        spiral.append(elems[0])
    return spiral[size - 1]


adj = [
    (-1, 1),  (0, 1),  (1, 1),
    (-1, 0),           (1, 0),
    (-1, -1), (0, -1), (1, -1),
]


def is_corner(p):
    return p[0] == p[1] or \
           (p[0] > 0 and p[0] == 1 - p[1]) or\
           (p[0] < 0 and p[0] == -p[1])


def solve2(limit):
    nums = {(0, 0): 1}
    p = (1, 0)
    d = (1, 0)
    s = 0

    while s < limit:
        nums[p] = s = sum(nums[(p[0] + q[0], p[1] + q[1])]
                          for q in adj if (p[0] + q[0], p[1] + q[1]) in nums)
        d = (-d[1], d[0]) if is_corner(p) else d
        p = (p[0] + d[0], p[1] + d[1])
    return s


print(solve1(361527))
print(solve2(361527))
