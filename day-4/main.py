#!/usr/bin/env python

import re

REGEX = re.compile("\d+")

def main():
    
    counter = 0

    with open("input.txt", "r") as file:
        for line in file:
            add_value = 0.5
            card = line.split(":")
            numbers = card[1].split("|")
            winning_numbers = REGEX.findall(numbers[0])
            scratched_numbers = REGEX.findall(numbers[1])
            print(winning_numbers, scratched_numbers)
            for num in scratched_numbers:
                for win in winning_numbers:
                    if num == win:
                        add_value = add_value * 2
                        print(f"Matched {num} at {winning_numbers.index(win)+1} = {add_value}")
            if add_value != 0.5:
                counter += add_value
                print(f"Added {add_value} to counter, is now {counter}")
            print("------------------------------")

    return counter
                        

if __name__=="__main__":
    solution = main()
    print(f"The sum is {solution}")