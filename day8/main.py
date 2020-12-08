# sam little
# aoc day 8

import copy
import time

with open('day8-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n')

instructions = []
for i in data:
    inst = {}
    temp = i.split(' ')
    inst['code'] = temp[0]
    inst['num'] = int(temp[1])
    inst['hasRun'] = False
    instructions.append(inst)


def run(program):
    pc = 0
    acc = 0
    lastJump = 0
    t_end = time.time() + 0.10
    while pc < len(program) and time.time() < t_end:
        # if(instructions[pc]['hasRun'] == True):
        #     break
        program[pc]['hasRun'] = True

        inst = program[pc]
        code = inst['code']
        num = inst['num']

        pc += 1

        if code == 'acc':
            acc += num
        elif code == 'jmp':
            lastJump = pc
            pc += num - 1
        elif code == 'nop':
            pass
        else:
            print('PANIC! unknown opcode')
            exit(1)

    if time.time() < t_end:
        print(acc, lastJump)
    else:
        print('ran out of time')


instructions_to_test = []
for idx, item in enumerate(instructions):
    p = {}
    old = ''
    new = ''
    prog = copy.deepcopy(instructions)
    if item['code'] == 'jmp':
        prog[idx]['code'] = 'nop'
        old = 'jmp'
        new = 'nop'
        p['desc'] = f'changed inst {idx} from {old} to {new}'
        p['prog'] = prog
        instructions_to_test.append(p)
    elif item['code'] == 'nop' and item['num'] != 0:
        prog[idx]['jmp'] = 'jmp'
        old = 'nop'
        new = 'jmp'
        p['desc'] = f'changed inst {idx} from {old} to {new}'
        p['prog'] = prog
        instructions_to_test.append(p)
    else:
        pass

while len(instructions_to_test) > 0:
    prog = instructions_to_test.pop()
    print(prog['desc'])
    run(prog['prog'])


run(instructions)
