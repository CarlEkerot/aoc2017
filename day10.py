from functools import reduce
from operator import xor


def parse():
    with open('day10.txt') as f:
        return f.read().strip()


def hash(lengths, lst, pos, skip):
    for l in lengths:
        lt = lst[:max(0, pos + l - len(lst))]
        rt = lst[pos:pos + l]
        r = (rt + lt)[::-1]
        wrap = pos + l > len(lst)
        lst[:max(0, pos + l - len(lst))] = r[len(rt):] if wrap else r[:len(lt)]
        lst[pos:pos + l] = r[:len(rt)] if wrap else r[len(lt):]
        pos = (pos + l + skip) % len(lst)
        skip += 1
    return lst, pos, skip


def solve1(data):
    lengths = (int(l) for l in data.split(','))
    lst, _, _ = hash(lengths, list(range(256)), 0, 0)
    return lst[0] * lst[1]


def solve2(data):
    lengths = [ord(c) for c in data] + [17, 31, 73, 47, 23]
    pos = skip = 0
    lst = list(range(256))
    for i in range(64):
        lst, pos, skip = hash(lengths, lst, pos, skip)
    chunks = [lst[i:i + 16] for i in range(0, len(lst), 16)]
    xor_sum = [reduce(xor, c) for c in chunks]
    return ''.join('%02x' % x for x in xor_sum)


print(solve1(parse()))
print(solve2(parse()))
