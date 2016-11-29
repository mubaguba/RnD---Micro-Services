from flask import Flask, jsonify,json, request
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

    def __init__(self, UserID, details):
        self.UserID = UserID
        self.details = details

@app.route('/', methods = ['GET'])   #Uses GET method to return all information in the database.
def index():
    return json.dumps([u.as_dict() for u in User.query.all()+Todo.query.all()])

@app.route('/<int:todo_ID>', methods = ['GET'])
def get(todo_ID):
    query = db.execute("select * from Todo")
    return {'todo': [dict(zip(tuple(query.keys()), i)) for i in query.cursor if i[1] == todo_ID]}

@app.route('/', methods = ['POST'])  #Uses POST method with same URL as GET method to add new information to Todo table.
def create_dev():
    todo = Todo(UserID = request.json["UserID"],details = request.json["details"])
    db.session.add(todo)
    db.session.commit()
    return  "It worked"

@app.route('/update/<int:todo_ID>', methods = ['PUT']) ##URL which updates what is related to the todo_ID
def update_todo(todo_ID):
    dev = Todo.query.get(todo_ID) ##Gets the id so it is based off id.
    dev.UserID = request.json["UserID"]
    dev.details = request.json["details"]
    db.session.add(dev)
    db.session.commit()
    return "Updates todo"

@app.route('/del/<int:todo_ID>', methods = ['DELETE']) ##URL which deletes whatever information is related to the todo_ID
def delete_dev(todo_ID):
    db.session.delete(Todo.query.get(todo_ID))
    db.session.commit() ##Commits to the database so it is deleted.
    return jsonify({'result': "deleted"}) ##Returns true if it works.


@app.before_first_request #Creates everything before the first request.
def startup():
    db.create_all()

if __name__ == '__main__':
    app.run()