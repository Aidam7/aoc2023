import re

gamesPower = list()
with open("input.txt", "r") as file:
    for line in file:
        rounds = line.split(";")
        minRedCount = 0
        minGreenCount = 0
        minBlueCount = 0
        id = re.search(r"Game (\d*)", line).group(1)
        for round in rounds:
            redCount = re.search(r"(\d*) red", round)
            greenCount = re.search(r"(\d*) green", round)
            blueCount = re.search(r"(\d*) blue", round)
            if redCount is not None:
                if int(redCount.group(1)) > minRedCount:
                    minRedCount = int(redCount.group(1))
            else:
                redCount = 0
            if greenCount is not None:
                if int(greenCount.group(1)) > minGreenCount:
                    minGreenCount = int(greenCount.group(1))
            else:
                greenCount = 0
            if blueCount is not None:
                if int(blueCount.group(1)) > minBlueCount:
                    minBlueCount = int(blueCount.group(1))
            else:
                blueCount = 0
        power = minRedCount * minGreenCount * minBlueCount
        print(id, power, minRedCount, minGreenCount, minBlueCount)
        gamesPower.append(power)
print(sum(gamesPower))
