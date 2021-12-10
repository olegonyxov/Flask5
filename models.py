from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
engine = create_engine('sqlite:///Test3.sqlite')

movie_genre = Table("movies_genres", Base.metadata,
                    Column('genres_pk', Integer, ForeignKey('genres.pk')),
                    Column('movies_pk', Integer, ForeignKey('movies.pk')))


class Movie(Base):
    __tablename__ = "movies"
    pk = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)
    pempa = Column(String(80), unique=False, nullable=True)
    uppdate = Column(Date, nullable=True)


class Genre(Base):
    __tablename__ = "genres"
    pk = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    name = Column(String(80), unique=True, nullable=False)
    movies = relationship("Movie",
                          secondary=movie_genre,
                          backref="movies")


if __name__ == "__main__":
    Base.metadata.create_all(engine)
