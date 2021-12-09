import os
import sqlite3
from flask import Flask, render_template, request, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Test3.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.urandom(32)
db = SQLAlchemy(app)


#
@app.route("/movie", methods=['POST', 'GET'])
def login_form():

    if request.method == 'GET':
        return """
                 <form action='http://localhost:5000/movie', method='POST'>
                     <input name="moviename">
                     <input name="pempa">
                     <input type="submit">
                 </form>
                """
    elif request.method == 'POST':
        mlist=[]
        plist=[]
        moviename = request.form['moviename']
        pempa = request.form['pempa']
        conn = sqlite3.connect('Test3.sqlite')
        cur=conn.cursor()
        if moviename:
            mname =cur.execute(f'SELECT * FROM movie WHERE name="{moviename}"')
            for i in mname:
                mlist.append(i)
            print(mlist)
        if pempa:
            pname = cur.execute(f'SELECT * FROM movie WHERE pempa="{pempa}"')
            for i in pname:
                mlist.append(i)
            print(plist)
        response = make_response(render_template('movietemp.html', mlist=mlist, plist=plist))
        return response


# mlist=[]
# conn = sqlite3.connect('Test3.sqlite')
# cur=conn.cursor()
# mname =cur.execute(f'SELECT * FROM movie WHERE name = "firstmovie"')
# for i in mname:
#     mlist.append(i)
#     print(i)
# print(mlist)