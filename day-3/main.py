import re

DEC_REGEX = re.compile("\d+")
SYM_REGEX = re.compile("[^.|\d|\n|\s]")

all_digits = []

counter = 0

with open("input.txt", "r") as file:
    at_line = 1
    for line in file:
        start_at = 0
        digit_list = DEC_REGEX.findall(line)
        print(f"Line {at_line}: {digit_list}")
        for match in digit_list:    
            match_regex = re.compile(match)
            digit = match_regex.search(line, start_at)
            all_digits.append(
                {
                    "number": match,
                    "from-line": at_line - 1,  # range upward that can be adjacent
                    "to-line": at_line + 1,  # range downward that can be adjacent
                    "from-column": digit.start(),  # from before the match
                    "to-column": digit.end() + 1,  # to after the match
                }
            )
            start_at = digit.end() + 1
            print(f"Appended {all_digits[-1]}")

        at_line += 1
        print("------------------------------------")

with open("input.txt", "r") as file:
    at_line = 1
    for line in file:
        symbol_list = SYM_REGEX.findall(line)
        print(f"Line {at_line} symbols matched: {symbol_list}")
        start_at = 0
        for match in symbol_list:
            print(f"Matches for: {match}")
            symbol = line.find(match, start_at) + 1
            for item in all_digits:
                if (
                    symbol >= item["from-column"]
                    and symbol <= item["to-column"]
                    and at_line >= item["from-line"]
                    and at_line <= item["to-line"]
                ):
                    print(f"Match! {symbol}|{at_line} with {item['from-column']}-{item['to-column']}|{item['from-line']+1}")
                    counter += int(item["number"])
                    print(f"Added {int(item['number'])}; Counter now is {counter}")
                    print(item)
                    all_digits.remove(item)

            start_at = symbol + 1
            print("----------------------")

        at_line += 1
        print("+++++++++++++++++++++++++++++++++++++++++++++++")

print(f"The sum is (hopefully): {counter}")