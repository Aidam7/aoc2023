import re

replacements = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five":5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
calibration = list()
with open('input.txt', 'r') as file:
    for line in file:
        firstDig = re.search(r'^.*?(\d|one|two|three|four|five|six|seven|eight|nine)', line).group(1)
        secondDig = re.search(r'^.*(\d|one|two|three|four|five|six|seven|eight|nine)', line).group(1)
        if firstDig in replacements:
            firstDig = replacements[firstDig]
        if secondDig in replacements:
            secondDig = replacements[secondDig]
        #God forgive me for this
        calibration.append(int(str(firstDig)+str(secondDig)))
print(sum(calibration))