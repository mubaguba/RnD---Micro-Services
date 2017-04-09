import sqlite3
from bottle import route,run, request,get,post, delete

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM User")
    result = c.fetchall()
    c.close()
    return str(result)

@get('/todo/<id>')
def getOne(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("Select * from User where User_ID = (?)", (id))
    result = "User Name: "+ c.fetchall()
    c.execute("Select * from Todo where UserID = (?)", (id))
    result += "Todo Detail: " + c.fetchall()
    c.close()
    return str(result)
	

#@route('/new', method = 'GET')


run(debug=True, reloader=True)
