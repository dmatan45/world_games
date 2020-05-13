from currency_converter import CurrencyConverter
from datetime import date
from random import randrange
from WorldOfGames.live import difficulty

def get_money_interval():
    game_level = difficulty()
    d = game_level
    c = CurrencyConverter()
    t = c.convert(1, 'USD', 'ILS', date=date(2019, 2, 21))  # how to put the date today?
    system_choose = randrange(1, 100)
    print('The rate is:', round(t, 2))
    print('The game choose:', system_choose, '$')
    money_interval = (t * system_choose - (5 - d)), (t * system_choose + (5 - d))

    user_guess = int(input('Guess what the ILS value:'))
    print(money_interval[0] < user_guess < money_interval[1])

def play_CG():
    get_money_interval()


