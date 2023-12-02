import re

regex = re.compile('\d')
count = 0

with open("input.txt", "r") as file:
    for line in file:
        print(f"Original line is {line}")
        decimals = regex.findall(line)
        print(decimals)
        calibration_code = decimals[0] + decimals[-1]
        print(calibration_code)
        count += int(calibration_code)

print(f"The sum is: {count}")
