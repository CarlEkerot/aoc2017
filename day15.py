def parse():
    with open('day15.txt') as f:
        return tuple(int(l.split(' ')[-1]) for l in f)


fac_a, fac_b = (16807, 48271)
div = 0x7fffffff


def solve1(a, b):
    count = 0
    for i in range(40000000):
        a = (a * fac_a) % div
        b = (b * fac_b) % div
        if a & 0xffff == b & 0xffff:
            count += 1
    return count


def solve2(a, b):
    count = 0
    for i in range(5000000):
        while a & 0b11:
            a = (a * fac_a) % div
        while b & 0b111:
            b = (b * fac_b) % div
        if a & 0xffff == b & 0xffff:
            count += 1
        a = (a * fac_a) % div
        b = (b * fac_b) % div
    return count


print(solve1(*parse()))
print(solve2(*parse()))
