import page_loader
import teams_module
import pickle
from classes import Player
from classes import Game


# Will return a list of Player objects from basketball-reference
def get_all_player_stats():
    doc = page_loader.load_page("https://www.basketball-reference.com/leagues/NBA_2022_per_game.html")
    players = doc.find_all("tr", "full_table")

    all_players = {}
    found = []
    for player in players:
        info = player.find_all("td")
        stats = {}
        for i in info:
            stat_name = i.attrs['data-stat']
            if stat_name == 'player':
                player_name = i.text
            else:
                stats[stat_name] = i.text
        if player_name not in found:
            all_players.update({player_name: Player(player_name, stats)})
            found.append(player_name)
        else:
            print(f"Found {player_name} already")
    return all_players


def load_all_rosters(teams, all_stats):
    for team in teams:
        doc = page_loader.load_page(f"https://www.basketball-reference.com/teams/{team.short_name}/2022.html")
        rows = doc.find("tbody").find_all("tr")
        for row in rows:
            name = row.find("td", {"data-stat": "player"}).text.replace("(TW)", "").strip()
            player = all_stats.get(name)
            if player is not None:
                team.players.update({name: player})
            # else:
            #     print(f"Unable to find {name} from {team.short_name}")


def load_team_schedules(teams):
    for team in teams:
        doc = page_loader.load_page(f"https://www.basketball-reference.com/teams/{team.short_name}/2022_games.html")
        rows = doc.find("tbody").find_all("tr")
        for row in rows:
            try:
                date = row.find("td", {"data-stat": "date_game"}).text
                opponent = row.find("td", {"data-stat": "opp_name"}).text
                result = row.find("td", {"data-stat": "game_result"}).text
                pts_for = row.find("td", {"data-stat": "pts"}).text
                pts_against = row.find("td", {"data-stat": "opp_pts"}).text
                game = Game(date, opponent, result, pts_for, pts_against)
                team.games.append(game)
            except:
                do_nothing = True


def save_data():
    local_teams = teams_module.all_teams_reference.copy()
    print("Loading Stats")
    all_stats = get_all_player_stats()
    print("Loading Rosters")
    load_all_rosters(local_teams, all_stats)
    print("Loading Schedules")
    load_team_schedules(local_teams)

    f = open('data', 'wb')
    pickle.dump(local_teams, f)
    f.close()

def load_data():
    f = open('data', 'rb')
    local_teams = pickle.load(f)
    f.close()
    return local_teams

# save_data()
all_teams = load_data()
print()