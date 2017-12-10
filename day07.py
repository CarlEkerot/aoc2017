import re
from collections import Counter


def parse():
    programs = {}
    with open('day07.txt') as f:
        for line in f:
            m = re.match(r'(\w+) \((\d+)\)( -> (.*))?', line)
            name = m.group(1)
            weight = int(m.group(2))
            children = m.group(4).split(', ') if m.group(4) else []
            programs[name] = [weight, children, None]
        for name, (_, children, _) in programs.items():
            for c in children:
                programs[c][2] = name
    return programs


def solve1(programs):
    return [p for p, (_, _, parent) in programs.items() if not parent][0]


def solve2(root, programs):
    weight, children, _ = programs[root]
    weights = [solve2(c, programs) for c in children]
    if weights[1:] != weights[:-1]:
        counter = Counter(weights)
        good_weight = max(counter, key=counter.get)
        bad_weight = min(counter, key=counter.get)
        bad_idx = weights.index(bad_weight)
        child_weight = programs[children[bad_idx]][0]
        print(child_weight + (good_weight - bad_weight))
    return weight + sum(weights)


programs = parse()
root = solve1(programs)
print(root)

solve2(root, programs)
