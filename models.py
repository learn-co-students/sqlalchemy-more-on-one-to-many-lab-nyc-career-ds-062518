from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


# write the Player, City, Sport and Team tables below
class Player(Base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    number = Column(Integer, default = None)
    height = Column(Text)
    weight = Column(Float)
    age = Column(Integer)
    name = Column(Text)
    team_id = Column(Integer, ForeignKey('teams.id'))
    team = relationship("Team", back_populates='players')
class Team(Base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    city_id = Column(Integer, ForeignKey('cities.id'))
    sport_id = Column(Integer, ForeignKey('sports.id'))
    players = relationship("Player", order_by = "Player.number", back_populates='team')
    city = relationship("City", back_populates='teams')
    sport = relationship("Sport", back_populates='teams')
class Sport(Base):
    __tablename__ = 'sports'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    teams = relationship("Team", back_populates='sport')
class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    state = Column(Text)
    teams = relationship("Team", back_populates='city')


engine = create_engine('sqlite:///sports.db')
Base.metadata.create_all(engine)

#lazy='dynamic'
