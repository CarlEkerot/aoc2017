def parse():
    with open('day04.txt') as f:
        return (l.split() for l in f.readlines())


def solve1(phrases):
    return len([p for p in phrases if len(p) == len(set(p))])


def solve2(phrases):
    s = ([''.join(sorted(w)) for w in p] for p in phrases)
    return len([p for p in s if len(p) == len(set(p))])


print(solve1(parse()))
print(solve2(parse()))
