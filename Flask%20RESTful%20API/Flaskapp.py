from flask import Flask, jsonify,json, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('Config.py')
db = SQLAlchemy(app)

class JsonModel(object): #Class for making objects JSON serializable
    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

class User(db.Model, JsonModel): #Class which is a model for the User table in the database
    User_ID = db.Column(db.Integer, primary_key = True)
    FirstName = db.Column(db.String(20))
    LastName = db.Column(db.String(20))

    def __init__(self,User_ID,FirstName, LastName):
        self.User_ID = User_ID
        self.FirstName = FirstName
        self.LastName = LastName

class Todo(db.Model, JsonModel):    #Class which is a model for the Todo table in the database
    todo_ID = db.Column(db.Integer, primary_key = True)
    UserID = db.Column(db.Integer, db.ForeignKey("user.User_ID"))
    details = db.Column(db.String(30))

    def __init__(self,todo_ID, UserID,details):
        self.todo_ID = todo_ID
        self.UserID = UserID
        self.details = details

@app.route('/', methods = ['GET'])   #Uses GET method to return all information in the database.
def index():
    return json.dumps([u.as_dict() for u in User.query.all()+Todo.query.all()])

@app.route('/todo/<int:UserID>', methods = ['GET'])
def get(UserID):
    return (list[Todo.query.get(UserID)])

@app.route('/', methods = ['POST'])  #Uses POST method with same URL as GET method to add new information to Todo table.
def create_dev():
    dev = Todo(request.json["todo_ID"], request.json["UserID"], request.json["details"])
    db.session.add(dev)
    db.session.commit()
    return json.dumps([{'dev': dev}]), 201

@app.before_first_request #Creates everything before the first request.
def startup():
    db.create_all()

if __name__ == '__main__':
    app.run()