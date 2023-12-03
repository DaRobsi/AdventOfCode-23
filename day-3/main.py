import re

DEC_REGEX = re.compile("\d+")
CHAR_REGEX = re.compile("[^.|\d]")

with open("input.txt", "r") as file:
    i = 1
    for line in file:
        matches = DEC_REGEX.findall(line)
        print(f"Line {i}: {matches}")
        for match in matches:
            start = line.find(match)
            end = line.rfind(match)


        i += 1