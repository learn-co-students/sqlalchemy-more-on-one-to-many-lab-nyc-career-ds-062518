from models import *
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///sports.db')

Session = sessionmaker(bind=engine)
session = Session()

# below we are reading the csv files to create the data we will need to create the players
# pandas returns a DataFrame object from reading the CSV
# we then tell the DataFrame object to turn each row into dictionaries
# by giving to_dict the argument "orient='records'"
# we are telling our DataFrame to make each row a dictionary using the column headers
# as the keys for the key value pairs in each new dictionary
# feel free to uncomment lines 18-21 to see each step of the process in your terminal
# ____ example ______
# la_dodgers0 = pd.read_csv('la_dodgers_baseball.csv')
# la_dodgers1 = pd.read_csv('la_dodgers_baseball.csv').to_dict()
# la_dodgers2 = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
# import pdb; pdb.set_trace()
# __________________
la_dodgers = pd.read_csv('la_dodgers_baseball.csv').to_dict(orient='records')
la_lakers = pd.read_csv('la_lakers_basketball.csv').to_dict(orient='records')
ny_yankees = pd.read_csv('ny_yankees_baseball.csv').to_dict(orient='records')
ny_knicks = pd.read_csv('ny_knicks_basketball.csv').to_dict(orient='records')

baseball = Sport(name = 'baseball')
basketball = Sport(name = 'basketball')
team_la_dodgers = Team(name = 'L.A. Dodgers')
team_la_lakers = Team(name = 'L.A. Lakers')
team_ny_yankees = Team(name = 'NY Yankees')
team_ny_knicks = Team(name = 'NY Knicks')
city_NY = City(name = 'New York')
city_LA = City(name = 'Los Angeles')

session.commit()

list_team_obj_csv = [(la_dodgers,team_la_dodgers,city_LA,baseball),(la_lakers,team_la_lakers,city_LA,basketball),(ny_yankees,team_ny_yankees,city_NY,baseball),(ny_knicks,team_ny_knicks,city_NY,basketball)]

# now that we have the data for each player
# add and commit the players, teams, sports and cities below
# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first


def populate(team_csv, team_obj, city_obj, sport_obj):
    for element in team_csv:
        if 'number' not in element.keys():
            element['number'] = element.get('number', None)
        if 'age' not in element.keys():
            element['age'] = element.get('age', None)

    return_list = [Player(name = element['name'],
            height = element['height'],
            weight = element['weight'],
            number = element['number'],
            age = element['age']) for element in team_csv]

    team_obj.players = return_list
    team_obj.city = city_obj
    team_obj.sport = sport_obj

    session.add_all(return_list)
    session.commit()
    return return_list

for i in range(0,len(list_team_obj_csv)):
    populate(list_team_obj_csv[i][0],list_team_obj_csv[i][1], list_team_obj_csv[i][2], list_team_obj_csv[i][3])
