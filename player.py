class Player:
    def __init__(self):
        self._total_points = 0

    def modify_total_points(self, value):
        self._total_points =+ value

    def modify_round_points(self, value):
        self._round_points =+ value

    def get_player_total_points(self):
        return self._total_points
        