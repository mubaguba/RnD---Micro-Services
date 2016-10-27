from flask import Flask, request, jsonify,redirect, url_for
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

e = create_engine('sqlite:///C:/sqlite/list.db')
app = Flask(__name__)
api= Api(app)
#gets all unique details from the table.

#Still working on outputting everything from the database tables properly
class getEverything(Resource): #Class for getting everything from the database.
    def get(self):  #Method which implements the GET request method.
        conn = e.connect()  #variable for connecting to database.
        query = conn.execute("select * from User,todo") #runs the query which selects everything from both tables.
        return {'All information': [i for i in query.cursor.fetchall()]} #Returns everything from the query.



#gets the details of user_id when it is written in the url.
class tododetai(Resource):

    def get(self,User_ID):
        conn = e.connect()
        query = conn.execute("select * from todo")
        return {'todo': [dict(zip(tuple(query.keys()),i)) for i in query.cursor if i[1] == User_ID]}



api.add_resource(getEverything, '/' ,methods = ['GET'])
api.add_resource(tododetai, '/todo/<int:User_ID>')





#class posttodo(Resource):
 #   def post(self, User_ID):
  #      conn = e.connect()
   #     query = conn.execute("insert into todo (")
if __name__ == '__main__':
     app.run()
