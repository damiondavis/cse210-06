from score import Score

class bot_score(Score):
    """
    add points for the bot score
    """
    s = Score
    def total_score(score):
        bot_score = s.total_score