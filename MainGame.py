from WorldOfGames.live import load_game
from WorldOfGames.CurrencyRouletteGame import play_CG
from WorldOfGames.GuessGame import play_GG
from WorldOfGames.MemoryGame import play_MG

def main_game():
    choose_game = load_game()
    if choose_game == 1:
        play_MG()

    elif choose_game == 2:
        play_GG()

    elif choose_game == 3:
        play_CG()

    else:
        return main_game()
main_game()



