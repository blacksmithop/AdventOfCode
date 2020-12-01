from itertools import combinations
from operator import mul
from functools import reduce

def santize(t: str):
    t = t.split('\n')
    t = map(int, t)
    t = list(t)
    return t


def findPairs(lst, K, N):
    return [pair for pair in combinations(lst, N) if sum(pair) == K][0]


if __name__ == '__main__':
    with open('input.txt') as f:
        text = f.read()

    nums = santize(text)
    n = int(input("How many elements?\n>"))
    ans = findPairs(nums, 2020, n)
    print(ans)  # numbers
    print(reduce(mul, ans, 1))