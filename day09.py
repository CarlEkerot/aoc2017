def parse():
    with open('day09.txt') as f:
        yield from f.read()


def solve(stream):
    score = 0
    mul = 0
    num_garbage = 0
    garbage = False
    skip = False
    for c in stream:
        if skip:
            skip = False
        elif c == '!':
            skip = True
        elif garbage and c != '>':
            num_garbage += 1
        elif garbage and c == '>':
            garbage = False
        elif c == '<':
            garbage = True
        elif c == '{':
            mul += 1
        elif c == '}':
            score += mul
            mul -= 1
        else:
            pass
    return score, num_garbage


print(solve(parse()))
