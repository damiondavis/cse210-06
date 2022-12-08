import dice as d
from score import Score
choice = 'done'

#Assign the total rolls and kept rolls to lists in dice file

class Choice(d, Score):
    kept_rolls = d.kept_rolls
    rolls = d.rolls


    def die_selection(self):

        #Open the rules file and print it at the top of the terminal each time the user has the option to select dice
        with open("rules.txt", "r", encoding="utf-8") as rules:
            for line in rules:
                print(line.strip())

        #Display the current rolls to the player
        print(f'Your roll looks like this {d.rolls}')
        #Allows the user to enter which dice #'s they want to keep, seperated by commas
        keep_input = input('Which dice do you want to keep (comma seperated: (e.g 1,1,5)? ')
        split_input = keep_input.split(',')

        #Adds the user's selection to the kept rolls list
        split_input_int = [int(item) for item in split_input]
        for die in split_input_int:
            d.kept_rolls.append(die)

        #if the user types 'done' they will be finished selecting dice
        if keep_input == 'done':
            return d.kept_rolls
        else:
            print('Invalid input, please try again.')

        #remove the selected dice from the current rolls
        for value in split_input_int:
            if value in d.rolls:
                d.rolls.remove(value)
        return d.rolls

        #This is where we would want to reroll the remaining die - JW


    def show_updates(total_points):
        print(f'Your total score is {Score.total_points}')
        print(f'Your kept rolls are {d.kept_rolls}')
