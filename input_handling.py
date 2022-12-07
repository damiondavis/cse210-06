import dice as d

choice = 'done'

class Choice:
    def die_selection():
        input('Choose a die to keep.')
        if choice.lower() != 'done':
            choice = input('Choose another die or type DONE to finish choosing.')
            
# Inputs the player should be allowed to make
# A list of all the choices they have available (like a controls menu)
# See the rules displayed on screen (this will be grabbed from the txt file)
# See the score conditions diplayed on screen
# See their current score
# See what dice they have kept so far
# Choose which die they want to keep (one at a time)
# Finish choosing dice
