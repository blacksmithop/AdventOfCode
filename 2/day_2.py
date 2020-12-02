def part1(t: str):
    r, l, s = t.split()
    r = tuple(map(int, r.split('-')))
    l = l[0]
    occ = s.count(l)
    return r[0] <= occ <= r[1]


def part2(t: str):
    r, l , s = t.split()
    r = tuple(map(int, r.split('-')))
    l = l[0]
    b, e = r
    if (s[b-1] == l) ^ (s[e-1] == l):
        return True


if __name__ == '__main__':
    valid_1,valid_2 = 0, 0
    #Part 1
    with open('input.txt') as f:
        for text in f:
            if part1(text):
                valid_1 += 1
            if part2(text):
                valid_2 += 1
    print("Part1 ", valid_1)
    print("Part2 ", valid_2)

    #Part2

