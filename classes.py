class Team:
    def __init__(self, short_name, city, mascot):
        self.short_name = short_name
        self.city = city
        self.mascot = mascot
        self.players = {} # Dictionary {Name:Player Object}
        self.games = [] # List of Game Objects


class Player:
    def __init__(self, name, stats, injury_status=None):
        self.name = name
        self.stats = stats
        self.injury_status = injury_status


class Game:
    def __init__(self, date, opponent, result, pts_for, pts_against):
        self.date = date
        self.opponent = opponent
        self.result = result
        self.pts_for = pts_for
        self.pts_against = pts_against
