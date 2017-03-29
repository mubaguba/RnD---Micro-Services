import bottle
from bottle import Bottle
from bottle.ext import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, Sequence, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('todo.db')
app = Bottle()
plugin = sqlalchemy.Plugin(engine, keyword = 'db')

app.install(plugin)

class User(Base):
    __tablename__ = 'User'
    user_id = Column(Integer, primary_key=True)
    fName = Column(String)
    lName = Column(String)

@app.get("/")
def show(db):
    table_data = db.query(User)

    results = []

    for x in table_data:
        results.append({'name'})




app.run(debug=True, reloader=True)