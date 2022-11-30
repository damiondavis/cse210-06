import random as r

die_value = 0

# Player values
rolls = []
kept_rolls = []
new_points = 0

# Bot values
bot_rolls = []
bot_kept_rolls = []
bot_new_points = 0

class D:
    def roll(rolls,kept_rolls):
        while kept_rolls < 6:
            rolls.append(r.randint(1,6))
        for item in rolls:
            print(item, end=" - ")
    
    def bot_roll(bot_rolls,bot_kept_rolls):
        while bot_kept_rolls < 6:
            bot_rolls.append(r.randint(1,6))
        for item in bot_rolls:
            print(item, end=" - ")