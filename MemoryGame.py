import random
import time
from WorldOfGames.live import difficulty

def list_equal():
    game_level = difficulty()
    generate_sequence = [random.randrange(1, 101) for i in range(game_level)]
    print(generate_sequence)

    for i in range(10):
        print("-" * i)
        time.sleep(0.7)

    list_from_user = []
    n = len(generate_sequence)
    for i in range(0, n):
        ele = int(input("enter number: "))
        list_from_user.append(ele)
    print(list_from_user == generate_sequence)
def play_MG():
    return list_equal()







