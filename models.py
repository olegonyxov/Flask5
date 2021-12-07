from app import db


class Movie(db.Model):
    __tablename__ = "Movies"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    release_date = db.Column(db.Date)


class Genre(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        return '<User %r>' % self.username
