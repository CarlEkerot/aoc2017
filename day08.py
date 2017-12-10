import operator
import re
from collections import defaultdict


cmap = {
    '==': operator.eq,
    '!=': operator.ne,
    '<': operator.lt,
    '>': operator.gt,
    '<=': operator.le,
    '>=': operator.ge
}


def parse():
    with open('day08.txt') as f:
        p = re.compile(r'(\w+) (\w+) (-?\d+) if (\w+) (\S+) (-?\d+)')
        yield from (p.match(line).groups() for line in f)


def solve(ins):
    regs = defaultdict(lambda: 0)
    max_seen = float('-inf')
    for r, op, n, cr, cop, cn in ins:
        if cmap[cop](regs[cr], int(cn)):
            regs[r] += int(n) if op == 'inc' else -int(n)
        if regs[r] > max_seen:
            max_seen = regs[r]
    return max(regs.values()), max_seen


print(solve(parse()))
