import re

with open("input.txt") as file:
    points = 0
    for winningNum, line in enumerate(file):
        matchCount = 0
        line = re.sub(r"^Card +\d*: ", "", line)
        line = line.split("| ")
        winningNums = line[0]
        bettedNums = line[1]
        winningNums = [
            winningNums[i : i + 3].rstrip() for i in range(0, len(winningNums), 3)
        ]
        bettedNums = [
            bettedNums[i : i + 3].rstrip() for i in range(0, len(bettedNums), 3)
        ]
        for winningNum in winningNums:
            for bettedNum in bettedNums:
                if winningNum == bettedNum:
                    matchCount += 1
        if matchCount > 0:
            points += pow(2, matchCount - 1)
    print(points)
