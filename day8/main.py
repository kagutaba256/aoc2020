# sam little
# aoc day 8
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
    while pc < len(program):
        if(instructions[pc]['hasRun'] == True):
            break
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

    print(acc, lastJump)


run(instructions)
