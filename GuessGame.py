from WorldOfGames.live import difficulty
import random

def compare_result():

    level = difficulty()
    generate_number = random.randrange(1, level)
    user_guess = int(input("Choose number between 0 to your level: "))
    if user_guess < level and user_guess > 0:
        print(generate_number == user_guess)
    else:
        return compare_result()

def play_GG():
    compare_result()


