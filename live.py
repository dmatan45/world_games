def welcome():
    name = input(str("what is your name?\n"))
    print("Hello " + name.capitalize() + " and Welcome to the World of Games (wog)\nHere you can find many cool games to play.\n")

def load_game():
    print("please choose game to play:\n"
          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it bac\n"
          "2. Guess Game - guess a number and see if you chose like the computer\n"
          "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")
    my_choose = int(input("your choose:"))

    if my_choose == 1:
        return my_choose

    elif my_choose == 2:
        return my_choose

    elif my_choose == 3:
        return my_choose

    else:
        return load_game()

def difficulty():
    my_level = int(input("Please choose game difficulty from 1 to 5: "))
    if my_level > 0 and my_level < 6:
        return my_level
    else:
        return difficulty()
