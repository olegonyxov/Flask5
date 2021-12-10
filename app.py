from flask import Flask, render_template, request, make_response
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import Movie, Base

engine = create_engine('sqlite:///Test3.sqlite')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

app = Flask(__name__)
app.config.from_pyfile("app_config.cfg")


@app.route("/movie", methods=['POST', 'GET'])
def login_form():
    if request.method == 'GET':
        quer = session.query(Movie).all()
        querList = []
        for i in quer:
            q_gather = (i.name, i.uppdate)
            querList.append(q_gather)
        response = make_response(render_template('movietemp.html', querList=querList))
        return response
