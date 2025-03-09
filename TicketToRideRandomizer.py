import random
import colorsys
#this will randomly suffle a list of tasks

tasks = ["Take 1-5 cards", "Take a contract", "Pick a wheel for a chosen opponent","Take 1-5 contracts", "Wheel Of Fortune", "Wheel of curses", "Wheel of misfortune", "Trivia build in Amsterdam", "Trivia Build in New York", "Trivia Build In Europe" ,"Trivia get Contracts", "Trivia get 5 cards for each", "Random Wheel 1-5", "Act freely", "Block a road (max length 4)", "Lose 1-5 cards", "Lose 1-5 contracts", "Lose 1-5 trains", "Lose a station", "Get a station (doesn't count for bonus points)", "Steal a contract", "Steal 3 cards", "Give away 3 cards", "Get a contract and 5 cards from a different map 1-5", "Build", "Build", "Build", "Get 5 cards Amsterdam", "Get 5 cards New York", "Destroy an opponents road", "Trivia", "Wheel 1-5", "Get 5 cards from every map", "Destroy a construction on a map, build for free on another that's max the size - 1 of the one you destroyed", "Build on Amsterdam", "Build on World Map", "Build on New York", "Destroy an enemy's road", "Wheel of Improv", "Choose a wheel", "Pick 2 contracts", "Steal 1-5 cards from a chosen opponent", "Lose 10 cards, get 2 contracts and an extra station (does not count for final points)", "Build 1-5 times", "Build once on every map", "Build 2 times (max once per map)", "Build", "Say a praier", "Spin the improv wheel", "remove a bad effect from yourself"]

random.shuffle(tasks)

while True:
    random.shuffle(tasks)
    print("\n\n\n\n")
    print("0. Win the game")

    for i in range(len(tasks)):
        color = ""
        if i % 2 == 0:
            color = "\033[1;37;40m"
        else:
            color = "\033[1;37;41m"
        print(color + str(i+1) + ". " + tasks[i] + "\033[1;37;40m")

    i = input("Check task number(Or press enter to shuffle again): ")
    try:
        i = int(i)
        if type(i) == int and i == 0:
            print("\033[1;37;42m" + "You won the game!" + "\033[1;37;40m")
            input("Press enter to continue")
            break
        elif i < 0 or i > len(tasks):
            print("\033[1;37;41m" + "Invalid task number" + "\033[1;37;40m")
            input("Press enter to continue")
        else:
            if type(i) == int:
                    print("\033[1;37;41m" + tasks[i] + "\033[1;37;40m")
                    input("Press enter to continue")
            else:
                pass
    except:
        pass

