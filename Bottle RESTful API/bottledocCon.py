import sqlite3
from bottle import route, run

@route('/todo')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT * FROM User")
    result = c.fetchall()
    return str(result)

run(debug=True, reloader=True)