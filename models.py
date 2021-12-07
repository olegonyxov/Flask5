from app import db


movies_genres = db.table('movies_genres',
                db.Column('genres_pk', db.Integer, db.ForeignKey('genres.pk'), primary_key=True),
                db.Column('movies_pk', db.Integer, db.ForeignKey('movies.pk'), primary_key=True),
                )

class Movie(db.Model):
    __tablename__ = "movies"
    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    tags = db.relationship('Genres', secondary=movies_genres,
                           backref=db.backref('movies', lazy='dynamic'))


class Genre(db.Model):
    __tablename__ = "genres"
    pk = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    tags = db.relationship('movies', secondary=movies_genres,
                           backref=db.backref('genres', lazy='dynamic'))

db.create_all()
#
#
