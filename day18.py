from collections import defaultdict


def parse():
    with open('day18.txt') as f:
        return [l.strip().split(' ') for l in f]


class Program(object):
    def __init__(self, instructions, pid):
        self.regs = defaultdict(lambda: 0)
        self.regs['p'] = pid
        self.freq = None
        self.ip = 0
        self.instructions = instructions
        self.rx = []
        self.other = None
        self.num_sends = 0

    def val(self, v):
        return self.regs[v] if v in self.regs else int(v)

    def step(self):
        op = self.instructions[self.ip]
        if op[0] == 'set':
            self.regs[op[1]] = self.val(op[2])
        elif op[0] == 'mul':
            self.regs[op[1]] *= self.val(op[2])
        elif op[0] == 'add':
            self.regs[op[1]] += self.val(op[2])
        elif op[0] == 'mod':
            self.regs[op[1]] %= self.val(op[2])
        elif op[0] == 'jgz':
            self.ip += self.val(op[2]) if self.val(op[1]) > 0 else 1
            return
        elif op[0] == 'snd':
            if not self.other:
                self.freq = self.val(op[1])
            else:
                self.other.rx.insert(0, self.val(op[1]))
                self.num_sends += 1
        elif op[0] == 'rcv':
            if not self.other and self.val(op[1]) > 0:
                self.rx.append(self.freq)
            elif self.other and self.rx:
                self.regs[op[1]] = self.rx.pop()
            elif self.other:
                return
        self.ip += 1


def solve1(instructions):
    p = Program(instructions, 0)
    while not p.rx:
        p.step()
    return p.rx[0]


def solve2(instructions):
    p0 = Program(instructions[:], 0)
    p1 = Program(instructions[:], 1)
    p0.other = p1
    p1.other = p0
    prev_ips = (0, 0)
    while True:
        p0.step()
        p1.step()
        if prev_ips == (p0.ip, p1.ip):
            return p1.num_sends
        prev_ips = (p0.ip, p1.ip)


print(solve1(parse()))
print(solve2(parse()))
