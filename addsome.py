import datetime

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Movie, Genre, Base

engine = create_engine('sqlite:///Test3.sqlite')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


def add_some():
    date = datetime.date.today()
    genre1 = Genre(name="scary")
    movie1 = Movie(name='firstmovie', uppdate=date, pempa="scary")
    movie2 = Movie(name='secondmovie', uppdate=date, pempa="scary")
    movie3 = Movie(name='thirdmovie', uppdate=date, pempa="scary")
    session.add_all([movie1, movie2, movie3, genre1, ])
    session.commit()


if __name__ == "__main__":
    add_some()
