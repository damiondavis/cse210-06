import dice as d

class Score:
    """
    Have the scoring possabilities 
    """

    # If it is the players first turn it will check if the
    # player has the correct number of points to start the game
    first_turn == True

    def __init__(turn, die_value):
        if first_turn == True and die_value < 450:
            first_turn == True
        else:
            # If they have the correct numebr of points to start they begin
            first_turn == False

    # The term player is deciding if they call the player list or bot list
    def straight(die, player):
        for i in player:
            if player == 1 and player == 2 and player == 3 and player == 4 and player == 5 and player == 6:
                points = 4000
        total_points += points
        return total_points

    def three_of_a_kind(die, player):
        for i in player:
            for u in player:
                if i == u:
                    pairs += 1
                    if pairs == 3:
                        points = 3000
        total_points += points
        return total_points

    def ones(die, player):
        for i in player:
            if player == 1:
                # How many points they get for a single one
                points += 100
                # If they have three ones they get 1000 points
                if points == 300:
                    points = 1000
                # If they get four ones they get 2500 points
                elif points == 400:
                    points = 2500
                # If they get five ones they get 5500 points
                elif points == 500:
                    points = 5500
                # If they get six ones they get 7000 points
                elif points == 600:
                    # Player wins the game if they roll six ones
                    points = 10000
        total_points += points
        return total_points

    def fives(die, player):
        for i in player:
            if player == 5:
                # How many points they get for a single five
                points += 50
                # If they have three fives they get 1500 points
                if points == 150:
                    points = 1500
                # If they get four fives they get 1000 points
                elif points == 200:
                    points = 2000
                # If they get five fives they get 5000 points
                elif points == 250:
                    points = 5000
                # If they get six fives they get 7000 points
                elif points == 300:
                    points = 7000
        total_points += points
        return total_points

    def all_other_rolls(die, player):
        for i in player:
            if player == die and player != 1 and player != 5:
                points = 0
                number_roled += 1
                # If they have three of a number they get it multilied by 100
                if number_roled == 3:
                    points = (die * number_roled) * 100
                # If they get four of a number they get 1000 points
                elif number_roled == 4:
                    points = 2000
                # If they get five of a number they get 5000 points
                elif number_roled == 5:
                    points = 5000
                # If they get six of a number they get 7000 points
                elif number_roled == 6:
                    points = 7000
        total_points += points
        return total_points

