import re
from word2number.w2n import word_to_num


def part_1():
    regex = re.compile("\d")
    count = 0
    with open("input.txt", "r") as file:
        for line in file:
            print(f"Original line is {line}")
            decimals = regex.findall(line)
            print(decimals)
            calibration_code = decimals[0] + decimals[-1]
            print(calibration_code)
            count += int(calibration_code)
            print("------------------------")

    return count


# this solution is cursed as fuck, please don't use it
def part_2():
    number_list = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
    ]
    count = 0
    with open("input.txt", "r") as file:
        for line in file:
            matched_list = []
            print(f"Original line is {line}")
            for digit in number_list:
                if digit in line:
                    pos = line.find(digit)
                    rev_pos = line.rfind(digit)
                    if rev_pos != pos:
                        if isinstance(digit, str):
                            matched_list.append(
                                {"index": rev_pos, "match": word_to_num(digit)}
                            )
                        else:
                            matched_list.append({"index": rev_pos, "match": digit})
                    if isinstance(digit, str):
                        matched_list.append({"index": pos, "match": word_to_num(digit)})
                    else:
                        matched_list.append({"index": pos, "match": digit})

            matched_list.sort(key=lambda x: x["index"])
            print(matched_list)
            calibration_code = str(matched_list[0]["match"]) + str(
                matched_list[-1]["match"]
            )
            print(f"Calibration code is {int(calibration_code)}")
            count += int(calibration_code)
            print(f"The sum now is {count}")
            print("------------------------")

    return count


if __name__ == "__main__":
    p1 = part_1()
    p2 = part_2()
    print(f"The solutions are:\nPart 1: {p1}\nPart 2: {p2}")
