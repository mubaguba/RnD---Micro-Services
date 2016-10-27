import sqlite3
#Connects to the list database so we can create tables and insert data.
with sqlite3.connect('C:/sqlite/list.db') as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS User(UserID INTEGER PRIMARY KEY,
    FirstName text, LastName text)""")
    c.execute("""CREATE TABLE IF NOT EXISTS Todo(todo_ID INTEGER PRIMARY KEY, User_ID INTEGER, details text,
    FOREIGN KEY(User_ID) REFERENCES User(UserID))""")
    #Code for inserting all data into tables.
    c.execute("PRAGMA foreign_keys = on")
    c.execute("""INSERT INTO User (UserID, FirstName,LastName) values("1","Henry","Sen")""")
    c.execute("""INSERT INTO User (UserID, FirstName,LastName) values("2","Megan","Knox")""")
    c.execute("""INSERT INTO User (UserID, FirstName,LastName) values("3","Muba","Lenk")""")
    c.execute("""INSERT INTO User (UserID, FirstName,LastName) values("4","Steve","Cook")""")

    c.execute("""INSERT INTO todo(todo_ID, User_ID, details) Values("1","1","Clean the kitchen")""")
    c.execute("""INSERT INTO todo(todo_ID, User_ID, details) Values("2","2","Finish her Sprint 1")""")
    c.execute("""INSERT INTO todo(todo_ID, User_ID, details) Values("3","3","Work on all remaining Assignments")""")
    c.execute("""INSERT INTO todo(todo_ID, User_ID, details) Values("4","3","Document all his assignments")""")
    #This code won't work because there is no user_id 5 on the User table.
    #c.execute("""INSERT INTO todo(todo_ID, User_ID, details) Values("2","5","This won't work.""")