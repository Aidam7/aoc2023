import re

possibleGames = list()
with open("input.txt", "r") as file:
    for line in file:
        rounds = line.split(";")
        maxRedCount = 0
        maxGreenCount = 0
        maxBlueCount = 0
        id = re.search(r"Game (\d*)", line).group(1)
        for round in rounds:
            redCount = re.search(r"(\d*) red", round)
            greenCount = re.search(r"(\d*) green", round)
            blueCount = re.search(r"(\d*) blue", round)
            if redCount is not None:
                if int(redCount.group(1)) > maxRedCount:
                    maxRedCount = int(redCount.group(1))
            else:
                redCount = 0
            if greenCount is not None:
                if int(greenCount.group(1)) > maxGreenCount:
                    maxGreenCount = int(greenCount.group(1))
            else:
                greenCount = 0
            if blueCount is not None:
                if int(blueCount.group(1)) > maxBlueCount:
                    maxBlueCount = int(blueCount.group(1))
            else:
                blueCount = 0
        if maxRedCount <= 12 and maxGreenCount <= 13 and maxBlueCount <= 14:
            possibleGames.append(int(id))
            print(id, maxRedCount, maxGreenCount, maxBlueCount)
print(sum(possibleGames))
