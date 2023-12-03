RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

counter = 0

with open("input.txt", "r") as file:
    for game in file:
        red_min = 0
        green_min = 0
        blue_min = 0
        print(game)
        game_split = game.split(":")
        sets = game_split[1].split(";")
        for draw in sets:
            print(draw)
            ball_batch = draw.split(",")
            for balls in ball_batch:
                balls = balls.strip("\n")
                if "red" in balls and int(balls.strip("red")) > red_min:
                    red_min = int(balls.strip("red"))
                if "green" in balls and int(balls.strip("green")) > green_min:
                    green_min = int(balls.strip("green"))
                if "blue" in balls and int(balls.strip("blue")) > blue_min:
                    blue_min = int(balls.strip("blue"))

        counter_adder = red_min * green_min * blue_min
        print(f"The minimal balls in this game are:\nRed: {red_min}\nGreen: {green_min}\nBlue: {blue_min}")
        print(f"Therefore {counter_adder} is added to the sum")
        counter += counter_adder

        print("----------------------------")

    print(f"The sum is: {counter}")