import sqlite3
from bottle import route, run, debug, template, request

@route('/todo')
def todo_list():
    conn = sqlite3.connect('list.db')
    c = conn.cursor()
    c.execute("SELECT * FROM User ")
    result = c.fetchall()
    c.close()
    output = template('make_table', rows=result)
    return output

@route('/new', method='GET')
def new_user():

    new = request.GET.get('save','','').strip()
    conn = sqlite3.connect('list.db')
    c = conn.cursor()

    c.execute("INSERT INTO user (UserID,FirstName, LastName) VALUES (?,?,?)", (new,1))
    new_id = c.lastrowid

    conn.commit()
    c.close()

    return template('new_task.tpl')

debug(True)
run(reloader=True)