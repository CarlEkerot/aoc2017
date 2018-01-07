import re

pattern = r'''
In state ([A-Z]):
  If the current value is ([0-1]):
    - Write the value ([0-1]).
    - Move one slot to the (left|right).
    - Continue with state ([A-Z]).
  If the current value is ([0-1]):
    - Write the value ([0-1]).
    - Move one slot to the (left|right).
    - Continue with state ([A-Z]).
'''


def parse():
    with open('day25.txt') as f:
        text = f.read()
        start = re.findall(r'Begin in state ([A-Z])', text)[0]
        steps = int(re.findall(r'after (\d+)', text)[0])
        res = re.findall(pattern, text, re.MULTILINE)
        states = {}
        for s, v1, w1, m1, n1, v2, w2, m2, n2 in res:
            states[s] = [
                (int(w1), 1 if m1 == 'right' else -1, n1),
                (int(w2), 1 if m2 == 'right' else -1, n2),
            ]
        return states, start, steps


def solve(states, state, steps):
    tape = [0]
    pos = 0
    for i in range(steps):
        v = tape[pos]
        s = states[state]
        tape[pos] = s[v][0]
        pos += s[v][1]
        if pos < 0:
            tape.insert(0, 0)
            pos = 0
        elif pos >= len(tape):
            tape.append(0)
        state = s[v][2]
    return tape.count(1)


print(solve(*parse()))
