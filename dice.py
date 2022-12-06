import random as r
from input_handling import Choice

die_value = 0

# Player values
rolls = []
kept_rolls = []

# Bot values
bot_rolls = []
bot_kept_rolls = []

class D:
    def roll(rolls,kept_rolls,choice):
        if kept_rolls.count() == 6:
            print('You have no more dice to roll.')
            choice = 'done'
        else:
            while rolls < (6 - kept_rolls):
                rolls.append(r.randint(1,6))
            print(*rolls, sep = ' ')
    
    def bot_roll(bot_rolls,bot_kept_rolls):
        if bot_kept_rolls.count() == 6:
            print('no more dice for bot')
        else:
            while bot_rolls < (6 - bot_kept_rolls):
                bot_rolls.append(r.randint(1,6))
            print(*bot_rolls, sep = ' ')