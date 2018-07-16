from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    return session.query(City).filter_by(name = 'New York')[0].team
def return_players_for_la_dodgers():
    return session.query(Team).filter_by(name = 'L.A. Dodgers')[0].players
def return_sorted_new_york_knicks():
    return session.query(Team).filter_by(name = 'NY Knicks')[0].players
def return_youngest_basket_ball_player_in_new_york():
    return [obj[0] for obj in session.query(Player, Team).filter(Team.id == Player.team_id).filter(Team.name == 'NY Knicks').order_by(Player.age).all()][0]
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player
def return_all_players_in_los_angeles():
    return [_tuple[0].players for _tuple in session.query(Team,City).filter((Team.city_id == City.id) & (City.name == 'Los Angeles')).all()]
    # here we want to return all players that are associated with
    # a sports team in LA
def return_tallest_player_in_los_angeles():
    return session.query(Player).order_by(Player.height.desc()).all()[0]
    # here we want to return the tallest player associted with
    # a sports team in LA
def return_team_with_heaviest_players():
    return session.query(Player).order_by(Player.weight.desc()).all()[0].team
    # here we want to return the city with the players that
    # have the heaviest average weight (total weight / total players)
