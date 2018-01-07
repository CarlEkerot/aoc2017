def parse():
    with open('day23.txt') as f:
        return [l.strip().split(' ') for l in f]


def solve(instructions):
    regs = {r: 0 for r in 'abcdefgh'}

    def val(v):
        return regs[v] if v in regs else int(v)

    ip = 0
    mul_count = 0
    while 0 <= ip < len(instructions):
        op = instructions[ip]
        if op[0] == 'set':
            regs[op[1]] = val(op[2])
        elif op[0] == 'sub':
            regs[op[1]] -= val(op[2])
        elif op[0] == 'mul':
            regs[op[1]] *= val(op[2])
            mul_count += 1
        elif op[0] == 'jnz':
            ip += val(op[2]) if val(op[1]) != 0 else 1
            continue
        ip += 1
    return mul_count


print(solve(parse()))
