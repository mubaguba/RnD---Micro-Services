import sqlite3
from bottle import route,run, request,get,post, delete, error

@get('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM User")
    result = c.fetchall()
    c.execute("SELECT * FROM Todo")
    result += c.fetchall()
    c.close()
    return str(result)

@get('/todo/<id>')
def getOne(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("Select * from User where User_ID = (?)", (id))
    result =  c.fetchall()
    c.execute("Select * from Todo where UserID = (?)", (id))
    result +=  c.fetchall()
    c.close()
    return str(result)

@delete('/todo/delete/<id>')
def removeOne(id):
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("Delete from Todo where todo_ID = (?)", (id))
    conn.commit()
    result = c.fetchall()
    return str(result)

@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'



run(debug=True, reloader=True)
