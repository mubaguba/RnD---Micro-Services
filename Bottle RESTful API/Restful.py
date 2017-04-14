import bottle
import sqlite3
from bottle import route,run, request,get,post, delete, error

application = bottle.Bottle()

@application.route('/todo')
def todo_list():
    conn = sqlite3.connect('Practice.db')
    c = conn.cursor()
    c.execute("SELECT * FROM User")
    result = []
    result.append({'User table': c.fetchall()})
    c.execute("SELECT * FROM Todo")
    result.append({'Todo table': c.fetchall()})
    c.close()
    return str(result)

@application.route('/todo/<id>')
def getOne(id):
    conn = sqlite3.connect('Practice.db')
    c = conn.cursor()
    c.execute("Select * from User where User_ID = (?)", (id))
    result = []
    result.append({'User table': c.fetchall()})
    c.execute("Select * from Todo where UserID = (?)", (id))
    result.append({'Todo table': c.fetchall()})
    c.close()
    return str(result)

@application.route('/animal')
def addOne():
    conn = sqlite3.connect('Practice.db')
    c = conn.cursor()
	#new_animal = {'UserID' : request.json.get('UserID'), 'details' : request.json.get('Details')}
	#animals.append(new_animal)
	#return {'animals' : animals}
    return''

@application.route('/todo/delete/<id>')
def removeOne(id):
    conn = sqlite3.connect('Practice.db')
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

if __name__ == '__main__':
    application.run()

