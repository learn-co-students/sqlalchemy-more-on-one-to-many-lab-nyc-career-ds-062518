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

dodgers=Team(name='LA Dodgers', city_id=1, sport_id=2)
lakers=Team(name='LA Lakers', city_id=1, sport_id=1)

yankees=Team(name='NY Yankees', city_id=2, sport_id=2)
knicks=Team(name='NY Knicks', city_id=2, sport_id=1)

la=City(name='Los Angeles', state='California')
ny=City(name='New York', state='New York')

basketball=Sport(name='Basketball')
baseball=Sport(name='Baseball')


def heightconvert(height):
   string = ''.join(char for char in height if char.isalnum())
   feet = int(string[0])
   inches = int(string[1:])
   return feet * 12 + inches

for player in la_dodgers:
    session.add(Player(name=player['name'], number=player['number'], height=heightconvert(player['height']), weight=player['weight'], team_id=1))
    session.commit()

for player in la_lakers:
    session.add(Player(name=player['name'], number=player['number'], height=heightconvert(player['height']), weight=player['weight'], team_id=2, age=player['age']))
    session.commit()

for player in ny_yankees:
    session.add(Player(name=player['name'], height=heightconvert(player['height']), weight=player['weight'], team_id=3))
    session.commit()

for player in ny_knicks:
    session.add(Player(name=player['name'], number=player['number'], height=heightconvert(player['height']), weight=player['weight'], team_id=4, age=player['age']))
    session.commit()


session.add(dodgers)
session.add(lakers)
session.add(yankees)
session.add(knicks)
session.add(la)
session.add(ny)
session.add(basketball)
session.add(baseball)
session.commit()


# now that we have the data for each player
# add and commit the players, teams, sports and cities below
# we will need to probably write at least one function to iterate over our data and create the players
# hint: it may be a good idea to creat the Teams, Cities, and Sports first
