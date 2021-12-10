from flask import Flask, render_template, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Movie, Base

app = Flask(__name__)
app.config.from_pyfile("app_config.cfg")

engine = create_engine('sqlite:///Test3.sqlite')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()


@app.route("/movie", methods=['GET'])
def get_movies():
    quer = session.query(Movie).all()
    querList = []
    for i in quer:
        q_gather = (i.name, i.uppdate)
        querList.append(q_gather)
    response = make_response(render_template('movietemp.html', querList=querList))
    return response
