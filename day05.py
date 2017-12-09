def parse():
    with open('day05.txt') as f:
        return list(map(int, f.readlines()))


def solve(ins, inc):
    pos = 0
    steps = 0
    while 0 <= pos < len(ins):
        ins[pos] += inc(ins[pos])
        pos += ins[pos] - 1
        steps += 1
    return steps


print(solve(parse(), lambda i: 1))
print(solve(parse(), lambda i: -1 if i > 3 else 1))
