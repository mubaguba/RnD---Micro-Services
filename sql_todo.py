import sqlite3

con = sqlite3.connect('todo.db') # Warning: This file is created in the current directory
con.execute("CREATE TABLE todo (id INTEGER PRIMARY KEY, task char(100) NOT NULL, status bool NOT NULL)")
con.execute("INSERT INTO todo (task,status) VALUES ('Upskill Bottle',0)")
con.execute("INSERT INTO todo (task,status) VALUES ('Upskill Flask',1)")
con.execute("INSERT INTO todo (task,status) VALUES ('Upskill Docker',1)")
con.commit()