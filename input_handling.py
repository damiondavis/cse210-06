import dice as d

choice = 'done'

class Choice:
    def die_selection():
        input('Choose a die to keep.')
        if choice.lower() != 'done':
            choice = input('Choose another die or type DONE to finish choosing.')