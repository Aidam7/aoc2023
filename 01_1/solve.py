import re

calibration = list()
with open('input.txt', 'r') as file:
    for line in file:
        firstDig = re.search(r'^.*?(\d)', line).group(1)
        secondDig = re.search(r'^.*(\d)', line).group(1)
        calibration.append(int(firstDig+secondDig))
print(sum(calibration))