import re
passports = open('input.txt').read().strip().split('\n\n')

fields = dict(byr=lambda x: len(x) <= 4 and 2002 >= int(x) >= 1920,
              iyr=lambda x: len(x) <= 4 and 2020 >= int(x) >= 2010,
              eyr=lambda x: len(x) <= 4 and 2030 >= int(x) >= 2020,
              hgt=lambda x: (x.endswith('cm') and 193 >= int(x[:-2]) >= 150) or (
                          x.endswith('in') and 76 >= int(x[:-2]) >= 59),
              hcl=lambda x: re.match('^#[a-f\d]{6}$', x) is not None,
              ecl=lambda x: x in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
              pid=lambda x: len(x) == 9 and x.isdigit())
p1 = p2 = 0
for passport in passports:
    parts = re.split('\s', passport)
    passport_dict = dict(part.split(':') for part in parts)
    if all(key in passport_dict for key in fields):
        p1 += 1
        if all(fields[key](passport_dict[key]) for key in fields):
            p2 += 1
print(p1, p2)