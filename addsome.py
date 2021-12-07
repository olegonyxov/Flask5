from app import db
from models import Movie,Genre
movie1 = Movie(name='Movie1', email='admin@example.com')
guest = Genre(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()