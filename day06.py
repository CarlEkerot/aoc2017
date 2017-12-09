def parse():
    with open('day06.txt') as f:
        return [int(n) for n in f.readline().split()]


def solve(banks):
    states = {}
    cycles = 0
    while tuple(banks) not in states:
        states[tuple(banks)] = cycles
        m = max(range(len(banks)), key=lambda k: banks[k])
        num = banks[m]
        banks[m] = 0
        for i in range(1, num + 1):
            banks[(m + i) % len(banks)] += 1
        cycles += 1
    return cycles, cycles - states[tuple(banks)]


print(solve(parse()))
