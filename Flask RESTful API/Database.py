import sqlite3
#Connects to the list database so we can create tables and insert data.
with sqlite3.connect('/home/muba/PycharmProjects/Work/Practise.db') as connection:
    c = connection.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS User(User_ID INTEGER PRIMARY KEY,
    FirstName text, LastName text)""")
    c.execute("PRAGMA foreign_keys = on")
    c.execute("""CREATE TABLE IF NOT EXISTS Todo(todo_ID INTEGER PRIMARY KEY, UserID INTEGER,  details,
    FOREIGN KEY(UserID) REFERENCES User(User_ID))""")
    #Code for inserting all data into tables.

    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("1","Henry","Sen")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("2","Megan","Knox")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("3","Muba","Lenk")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("4","Steve","Cook")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("5","Mubasher","Khan")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("6","Jeff","Hardy")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("7","Matthew","Levine")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("8","Daniel","Potter")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("9","Chris","Sanders")""")
    c.execute("""INSERT INTO User (User_ID, FirstName,LastName) values("10","Mike","Hefferson")""")

    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("1","1","Clean the kitchen")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("2","2","Finish her Sprint 1")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("3","3","Work on all remaining Assignments")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("4","3","Document all his assignments")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("5","4","Starting studying for his exams")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("6","5","Clean his bedroom")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("7","6","Take the dog for a walk.")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("8","7","Go out and see the sun for the first time")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("9","8","Practise for upcoming soccer game")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("10","9","Catch the bus on time")""")
    c.execute("""INSERT INTO todo(todo_ID, UserID, details) Values("11","10","Go grocery shopping")""")

    #This code won't work because there is no user_id 5 on the User table.
    #c.execute("""INSERT INTO todo(todo_ID, User_ID, details) Values("2","5","This won't work.""")