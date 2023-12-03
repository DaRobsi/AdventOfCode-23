RED_MAX = 12
GREEN_MAX = 13
BLUE_MAX = 14

counter = 0

games = []

with open("input.txt", "r") as file:
    for line in file:

        is_under = True

        print(line)
        game = line.split(":")
        rounds = game[1].split(";")
        print(rounds)
        for items in rounds:
            sets = items.split(",")
            print(sets)
            print("Balls are:")
            for balls in sets:
                balls = balls.strip("\n")
                if "green" in balls:
                    green_balls = int(balls.strip("green"))
                    print(f"Green: {green_balls}")
                if "blue" in balls:
                    blue_balls = int(balls.strip("blue"))
                    print(f"Blue: {blue_balls}")
                if "red" in balls:
                    red_balls = int(balls.strip("red"))
                    print(f"Red: {red_balls}")

            if green_balls > GREEN_MAX or blue_balls > BLUE_MAX or red_balls > RED_MAX:
                is_under = False
                print("////////////////////////////////")
                green_balls = 0
                blue_balls = 0
                red_balls = 0
                break

            green_balls = 0
            blue_balls = 0
            red_balls = 0
            
        if is_under == True:
            counter += int(game[0].strip("Game"))
            games.append(int(game[0].strip("Game")))

        print("---------------------------")
    
    print(f"The sum of the game IDs is {counter}")
    print(f"The Games were: {games}")