from app import db


class Movie(db.Model):
    __tablename__ = "Movies"
    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    release_date = db.Column(db.Date)


class Genre(db.Model):
    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)


class MovieGenre(db.model):
    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    movie_pk = db.Column(db.Integer, db.ForeignKey("movies.pk"))
    genre_pk = db.Column(db.Integer, db.ForeignKey("genre.pk"))


