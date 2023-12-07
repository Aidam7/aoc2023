coordinates = []
adjacentNumbers = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def isSymbolAdjacent(startX, endX, y):
    for yCord in range(max(0, y - 1), min(y + 2, len(lines))):
        for xCord, char in enumerate(lines[yCord]):
            if (
                xCord == startX - 1
                or xCord == startX
                or xCord == startX + 1
                or xCord == endX - 1
                or xCord == endX
                or xCord == endX + 1
            ):
                if char != "." and not char.isnumeric():
                    return True
    return False


for y, line in enumerate(lines):
    startX = None
    endX = None
    number = ""
    for x, char in enumerate(line):
        if char.isnumeric():
            if startX is None:
                startX = x
            number += char
            if x + 1 == len(line) or not line[x + 1].isnumeric():
                endX = x
                coordinates.append([startX, endX, y, number])
                startX = None
                endX = None
                number = ""

for coordinate in coordinates:
    if isSymbolAdjacent(coordinate[0], coordinate[1], coordinate[2]):
        adjacentNumbers.append(int(coordinate[3]))
print(sum(adjacentNumbers))
