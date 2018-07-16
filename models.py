from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Player, City, Sport and Team tables below


class Sport(Base):
    __tablename__='sports'
    id = Column(Integer, primary_key=True)
    name=Column(Text)
    teams=relationship('Team', back_populates='sport')
    #has many teams

class City(Base):
    __tablename__='cities'
    id = Column(Integer, primary_key=True)
    name=Column(Text)
    state=Column(Text)
    teams=relationship('Team', back_populates='city')
    #has many teams

class Team(Base):
    __tablename__='teams'
    id = Column(Integer, primary_key=True)
    name=Column(Text)
    #has many players
    players=relationship('Player', back_populates='team')
    #belong to a City
    city_id=Column(Integer, ForeignKey('cities.id'))
    city=relationship('City', back_populates='teams')
    #belong to a sport
    sport_id=Column(Integer, ForeignKey('sports.id'))
    sport=relationship('Sport', back_populates='teams')

class Player(Base):
    __tablename__='players'
    id = Column(Integer, primary_key=True)
    name=Column(Text)
    number=Column(Integer, default=None)
    height=Column(Integer)
    weight=Column(Integer)
    #belong to a team
    team_id=Column(Integer, ForeignKey('teams.id'))
    team=relationship('Team', back_populates='players')
    age=Column(Integer)



engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
