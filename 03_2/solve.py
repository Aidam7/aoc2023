import re

coordinates = []
adjacentNumbers = []
with open("input.txt", "r") as file:
    lines = [line.strip() for line in file.readlines()]


def isGear(x, y):
    for yCord in range(max(0, y - 1), min(y + 2, len(lines))):
        for xCord, char in enumerate(lines[yCord]):
            num = ""
            if xCord == x - 1 or xCord == x + 1 or xCord == x:
                if char.isnumeric():
                    print(f"whole number {getWholeNumber(xCord, yCord)}")


def getWholeNumber(x, y):
    line = lines[y]
    match = re.search(r"\d+", line[x:])
    if match:
        return int(match.group())
    else:
        return None


for y, line in enumerate(lines):
    number = ""
    for x, char in enumerate(line):
        if char == "*":
            coordinates.append([x, y])
print(coordinates)
isGear(4, 1)
