if __name__ == '__main__':
    with open('input.txt') as f:
        mountain = f.read()
    height = mountain.count("\n") + 1
    mountain = mountain.replace("\n", "")
    width = int(len(mountain) / height)

    # Part 1
    trees = 0
    for x, y in zip((x % width for x in range(0, len(mountain), 3)), range(0, height, 1)):
        trees = trees + 1 if mountain[x + width * y] == "#" else trees

    print(f"P1 Trees: {trees}")

    # Part 2
    trees, trees_multiple, attempts = 0, 1, [1, 1, 3, 1, 5, 1, 7, 1, 1, 2]
    for i in range(0, len(attempts), 2):
        for x, y in zip((x % width for x in range(0, len(mountain), attempts[i])), range(0, height, attempts[i + 1])):
            trees = trees + 1 if mountain[x + width * y] == "#" else trees
        trees_multiple, trees = trees_multiple * trees, 0

    print(f"P2 Trees: {trees_multiple}")