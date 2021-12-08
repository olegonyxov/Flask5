from app import db
import datetime
from models import Movie,Genre,movie_genre
#
date=datetime.date.today()

movie1 = Movie(name='firstmovie')
movie2 = Movie(name='secondmovie')
movie3 = Movie(name='thirdmovie')
db.session.add(movie1)
db.session.commit()
