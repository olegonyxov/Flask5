from app import db

movie_genre = db.Table('movie_genre',
    db.Column('genre_id', db.Integer, db.ForeignKey('genre.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    pempa = db.Column(db.String(80), unique=False,nullable=True)
    uppdate = db.Column(db.String(80))
    movie_genre = db.relationship('Genre', secondary=movie_genre,
        backref=db.backref('movies', lazy='dynamic'))

class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


# db.create_all()


