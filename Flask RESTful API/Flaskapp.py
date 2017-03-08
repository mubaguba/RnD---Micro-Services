from flask import Flask, jsonify, json, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('Config.py')
db = SQLAlchemy(app)
response = {}


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

@app.route('/todo', methods = ['GET'])   #Uses GET method to return all information in the database.
def index():
    return json.dumps([u.as_dict() for u in Todo.query.all()])

@app.route('/todo/<int:todo_ID>', methods = ['GET'])
def get(todo_ID):
    response = jsonify()
    todoGet = {}
    todo = Todo.query.get(todo_ID)
    todoGet['todo_ID']= todo.todo_ID
    todoGet['UserID'] = todo.UserID
    todoGet['details'] = todo.details
    response.status_code = 201
    response.headers['location'] = '/todo/{}'.format(todo.todo_ID)
    return jsonify(todoGet)

@app.route('/todo', methods = ['POST'])  #Uses POST method with same URL as GET method to add new information to Todo table.
def create_todo():
    if not request.json:
        abort(400)
    response= jsonify()
    todo = Todo(UserID = request.json["UserID"],details = request.json["details"])
    db.session.add(todo)
    db.session.flush()
    db.session.commit()
    response.status_code = 201
    response.headers['location'] = '/todo/{}'.format(todo.todo_ID)
    return response

@app.route('/todo/<int:todo_ID>', methods = ['PUT']) ##URL which updates what is related to the todo_ID
def update_todo(todo_ID):
    response = jsonify()
    dev = Todo.query.get(todo_ID) ##Gets the id so it is based off id.
    dev.UserID = request.json["UserID"]
    dev.details = request.json["details"]
    db.session.add(dev)
    db.session.commit()
    response.status_code = 200
    response.headers['location'] = '/todo/{}'.format(dev.todo_ID)
    return response

@app.route('/todo/<int:todo_ID>', methods = ['DELETE']) ##URL which deletes whatever information is related to the todo_ID
def delete_dev(todo_ID):
    response = jsonify()
    db.session.delete(Todo.query.get(todo_ID))
    response.status_code = 204
    response.headers['location'] = '/todo/{}'.format(todo_ID)
    db.session.commit() ##Commits to the database so it is deleted.
    return response

@app.before_first_request #Creates everything before the first request.
def startup():
    db.create_all()

if __name__ == '__main__':
    app.run()