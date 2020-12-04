# sam little
# aoc day 4

with open('day4-input.txt', 'r') as f:
    data = f.read()

data = data.split('\n\n')
temp = []
for x in data:
    temp.append(x.replace('\n', ' '))

passports = []
for p in temp:
    passport = {}
    fields = p.split(' ')
    for f in fields:
        sp = f.split(':')
        passport[sp[0]] = sp[1]
    passports.append(passport)


def check_passport_valid(passport):
    required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for f in required_fields:
        if f not in passport.keys():
            return False

    if not passport['byr'].isnumeric():
        return False
    byr = int(passport['byr'])

    if not passport['iyr'].isnumeric():
        return False
    iyr = int(passport['iyr'])

    if not passport['eyr'].isnumeric():
        return False
    eyr = int(passport['eyr'])

    if len(passport['byr']) != len(passport['iyr']) != len(passport['eyr']) != 4:
        return False

    if not(1920 <= byr <= 2002):
        return False

    if not(2010 <= iyr <= 2020):
        return False

    if not(2020 <= eyr <= 2030):
        return False

    h = int(passport['hgt'][:len(passport['hgt'])-2])
    units = passport['hgt'][-2:]

    if units not in ['cm', 'in']:
        return False

    if units == 'cm':
        if not 150 <= h <= 193:
            return False
    else:
        if not 59 <= h <= 76:
            return False

    if not passport['hcl'].startswith('#'):
        return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(passport['pid']) != 9:
        return False

    return True


count = 0
for p in passports:
    if check_passport_valid(p):
        count += 1

print(count)
