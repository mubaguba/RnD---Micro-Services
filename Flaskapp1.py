from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///C:/sqlite/list.db')
app = Flask(__name__)
api= Api(app)
#gets all unique details from the table.
class tododetails(Resource):
    def get(self):
        conn = e.connect()
        query = conn.execute("select distinct details from todo")
        return {'details': [i[0] for i in query.cursor.fetchall()]}
api.add_resource(tododetails, '/')

#gets the details of user_id when it is written in the url.
class tododetai(Resource):
    def get(self,User_ID):
        conn = e.connect()
        query = conn.execute("select * from todo where User_ID <6")
        return {'todo': [dict(zip(tuple(query.keys()),i)) for i in query.cursor if i[1] == User_ID]}
api.add_resource(tododetai, '/todo/<int:User_ID>')

#class posttodo(Resource):
 #   def post(self, User_ID):
  #      conn = e.connect()
   #     query = conn.execute("insert into todo (")
if __name__ == '__main__':
     app.run()
