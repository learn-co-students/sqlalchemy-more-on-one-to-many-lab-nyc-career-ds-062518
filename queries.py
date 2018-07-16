from models import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

def return_teams_for_new_york():
    # here we want to return all teams that are associated with New York City
    return session.query(Team.name).filter_by(city_id = 2).all()


def return_players_for_la_dodgers():
    return session.query(Player.name).filter_by(team_id = 1).all()
    # here we want to return all players that are associated with the LA dodgers


def return_sorted_new_york_knicks():
    # here we want to return all the players on the New York Knicks
    # sorted in ascending (small -> big) order by their number
    return session.query(Player.name, Player.number).filter_by(team_id=4).order_by(Player.number.asc()).all()

def return_youngest_basket_ball_player_in_new_york():
    # here we want to sort all the players on New York Knicks by age
    # and return the youngest player

    youngest = session.query(Player, Sport).filter(Sport.name =='Basketball', City.name =='New York'). order_by(Player.age.asc()).all()
    return youngest
    #session.query(Player.name).filter_by(team_id=4).order_by(Player.age.asc()).first()


def return_all_players_in_los_angeles():
    # here we want to return all players that are associated with
    # a sports team in LA
    players_city =session.query(Player, city.name). filter(City.name == 'Los Angeles').all()
    players = [x[0] for x in players_city]
    return players

    #from sqlalchemy import or_
    #players= session.query(Player.name, Team.name).filter(or_(Team.name=='LA Dodgers', Team.name=='LA Lakers')).all()
    #return players

def return_tallest_player_in_los_angeles():
    # here we want to return the tallest player associted with
    # a sports team in LA

    players = session.query(Player, City.name).filter(City.name == 'Los Angeles').order_by(Player.height.desc()).first()
    return players[0]

def return_team_with_heaviest_players():
    from sqlalchemy import func
    session.query(Team, func.avg(Player.weight)).filter(Team.id).group_by(Team.id).all()

    team=session.query( func.avg(Player.weight), Team.name).group_by(Team.id).all()
    return team.name

    session.query(Team.name, func.avg(Player.weight)).filter(Player.team).group_by(Player.team).all()




    #session.query(Players).order_by(avg(Players.weight).asc()).first()
    # here we want to return the city with the players that
    # have the heaviest average weight (total weight / total players)
    #heaviest_guy=session.query(Player.team_id).order_by(Player.weight.desc()).first()
    #team=session.query(Team.name).filter_by(name=heaviest_guy).first()
    #return team
