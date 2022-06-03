from classes import Team

all_teams = {
    Team("bos", "Boston", "Celtic"),
    Team("bkn", "Brooklyn", "Nets"),
    Team('ny', "New York", "Knicks"),
    Team('phi', "Philadelphia", "76ers"),
    Team('tor', "Toronto", "Raptors"),
    Team('den', "Denver", "Nuggets"),
    Team('min', "Minnesota", "Timberwolves"),
    Team('okc', "Oklahoma City", "Thunder"),
    Team('por', "Portland", "Trail Blazers"),
    Team('utah', "Utah", "Jazz"),
    Team('chi', "Chicago", "Bulls"),
    Team('cle', "Cleveland", "Cavaliers"),
    Team('det', "Detroit", "Pistons"),
    Team('ind', "Indiana", "Pacers"),
    Team('mil', "milwaukee", "Bucks"),
    Team('gs', "Golden State", "Warriors"),
    Team('lac', "Los Angeles", "Clippers"),
    Team('lal', "Los Angeles", "Lakers"),
    Team('phx', "Phoenix", "Suns"),
    Team('sac', "Sacramento", "Kings"),
    Team('atl', "Atlanta", "Hawks"),
    Team('cha', "Charlotte", "Hornets"),
    Team('mia', "Miami", "Heat"),
    Team('orl', "Orlando", "Magic"),
    Team('wsh', "Washington", "Wizards"),
    Team('dal', "Dallas", "Mavericks"),
    Team('hou', "Houston", "Rockets"),
    Team('mem', "Memphis", "Grizzlies"),
    Team('no', "New Orleans", "Pelicans"),
    Team('sa', "San Antonio", "Spurs"),
}

all_teams_reference = [
    Team("BOS", "Boston", "Celtic"),
    Team("BRK", "Brooklyn", "Nets"),
    Team('NYK', "New York", "Knicks"),
    Team('PHI', "Philadelphia", "76ers"),
    Team('TOR', "Toronto", "Raptors"),
    Team('DEN', "Denver", "Nuggets"),
    Team('MIN', "Minnesota", "Timberwolves"),
    Team('OKC', "Oklahoma City", "Thunder"),
    Team('POR', "Portland", "Trail Blazers"),
    Team('UTA', "Utah", "Jazz"),
    Team('CHI', "Chicago", "Bulls"),
    Team('CLE', "Cleveland", "Cavaliers"),
    Team('DET', "Detroit", "Pistons"),
    Team('IND', "Indiana", "Pacers"),
    Team('MIL', "milwaukee", "Bucks"),
    Team('GSW', "Golden State", "Warriors"),
    Team('LAC', "Los Angeles", "Clippers"),
    Team('LAL', "Los Angeles", "Lakers"),
    Team('PHO', "Phoenix", "Suns"),
    Team('SAC', "Sacramento", "Kings"),
    Team('ATL', "Atlanta", "Hawks"),
    Team('CHO', "Charlotte", "Hornets"),
    Team('MIA', "Miami", "Heat"),
    Team('ORL', "Orlando", "Magic"),
    Team('WAS', "Washington", "Wizards"),
    Team('DAL', "Dallas", "Mavericks"),
    Team('HOU', "Houston", "Rockets"),
    Team('MEM', "Memphis", "Grizzlies"),
    Team('NOP', "New Orleans", "Pelicans"),
    Team('SAS', "San Antonio", "Spurs"),
]


def get_team(short_name=None, city=None, mascot=None):
    for team in all_teams:
        if team.short_name == short_name:
            return team
        if team.city == city:
            return team
        if team.mascot == mascot:
            return team

# all_teams = {
#     'bos': ["Boston", "Celtics"],
#     'bkn': ["Brooklyn", "Nets"],
#     'ny': ["New York", "Knicks"],
#     'phi': ["Philadelphia", "76ers"],
#     'tor': ["Toronto", "Raptors"],
#     'den': ["Denver", "Nuggets"],
#     'min': ["Minnesota", "Timberwolves"],
#     'okc': ["Oklahoma City", "Thunder"],
#     'por': ["Portland", "Trail Blazers"],
#     'utah': ["Utah", "Jazz"],
#     'chi': ["Chicago", "Bulls"],
#     'cle': ["Cleveland", "Cavaliers"],
#     'det': ["Detroit", "Pistons"],
#     'ind': ["Indiana", "Pacers"],
#     'mil': ["milwaukee", "Bucks"],
#     'gs': ["Golden State", "Warriors"],
#     'lac': ["Los Angeles", "Clippers"],
#     'lal': ["Los Angeles", "Lakers"],
#     'phx': ["Phoenix", "Suns"],
#     'sac': ["Sacramento", "Kings"],
#     'atl': ["Atlanta", "Hawks"],
#     'cha': ["Charlotte", "Hornets"],
#     'mia': ["Miami", "Heat"],
#     'orl': ["Orlando", "Magic"],
#     'wsh': ["Washington", "Wizards"],
#     'dal': ["Dallas", "Mavericks"],
#     'hou': ["Houston", "Rockets"],
#     'mem': ["Memphis", "Grizzlies"],
#     'no': ["New Orleans", "Pelicans"],
#     'sa': ["San Antonio", "Spurs"],
# }
#
#
# def get_city(short_name):
#     return all_teams.get(short_name)[0]
#
#
# def get_mascot(short_name):
#     return all_teams.get(short_name)[1]
#
#
# def get_full_name(short_name):
#     return f"{get_city(short_name)} {get_mascot(short_name)}"
#
#
# def get_short_name_from_mascot(mascot):
#     for short_name in all_teams:
#         if all_teams.get(short_name)[1] == mascot:
#             return short_name
#
#
# def get_short_name_from_city(city):
#     for short_name in all_teams:
#         if all_teams.get(short_name)[0] == city:
#             return short_name
