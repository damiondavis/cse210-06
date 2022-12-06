from player import Player as p

p = p()

class Computer:
    def __init__(self):
        self._base_risk = .5
        self._messages = ['Drat! I busted', 'Yay! I scored over 1000 points', 'Haha, you busted']
        self._total_points = 0
        self._round_points = 0

    def return_risk(self):
        return self._base_risk

    def return_message(self, num):
        return self._messages[num-1]

    def modify_total_points(self, value):
        self._total_points =+ value

    def modify_risk(self, change):
        self._base_risk = self._base_risk * change
        if self._base_risk > 1:
            self._base_risk = 1

    def risk_control(self):
        player_points = p.get_player_total_points()
        if self._points - player_points >= 2000:
            self.modify_risk(.8)
        elif self._points - player_points >= 1000:
            self.modify_risk(.9)

    def logic_determine(self):
        risk = self.return_risk()
        round_points = self._round_points
        if risk <= .4:
            if round_points >= 1000:
                return "stop"
            if round_points < 1000:
                return "roll"
        if risk > .4 and risk <= .6:
            if round_points >= 1250:
                return "stop"
            if round_points < 1250:
                return "roll"
        if risk > .6 and risk <= .8:
            if round_points >= 1750:
                return "stop"
            if round_points < 1750:
                return "roll"
        else:
            if round_points >= 2500:
                return "stop"
            if round_points < 2500:
                return "roll"
