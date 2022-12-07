from player import Player as p

p = p()

class Computer:
    def __init__(self):
        self._base_risk = .5
        self._messages = ['Drat! I busted', 'Yay! I scored over 1000 points', 'Haha, you busted']
        self._total_points = int(0)
        self._round_points = int(0)

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
        # The Computer will raise/lower its risk based upon whether it is further ahead or further behind.
        _player_points = p.get_player_total_points()
        if self._total_points - _player_points >= 2000:
            self.modify_risk(1.2)
        elif self._total_points - _player_points >= 1000:
            self.modify_risk(1.1)
        elif _player_points - self._total_points >= 1000:
            self.modify_risk(.9)
        elif _player_points - self._total_points >= 2000:
            self.modify_risk(.8)

    def logic_determine(self):
        risk = self.return_risk()

        # The Computer gets riskier as its risk level is higher and vice versa
        if risk <= .4:
            if self._round_points >= 1000:
                return "stop"
            if self._round_points < 1000:
                return "roll"
        if risk > .4 and risk <= .6:
            if self._round_points >= 1250:
                return "stop"
            if self._round_points < 1250:
                return "roll"
        if risk > .6 and risk <= .8:
            if self._round_points >= 1750:
                return "stop"
            if self._round_points < 1750:
                return "roll"
        else:
            if self._round_points >= 2500:
                return "stop"
            if self._round_points < 2500:
                return "roll"
