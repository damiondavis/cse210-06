from score import Score

class player_score(Score):
    """
    add points for the player score
    """
    s = Score
    def total_score(score):
        player_score = s.total_score