# RnD---Micro-Services
Repository for all code to do with the project

1. The Bottle folder has code which Kevin has developed.
2. The Flask folder has code which Mubasher has developed.

##SQL Statement
1. sqlite> select todo.todo_ID, todo.UserID, User.FirstName, todo.details from todo, User where todo.UserID = User.User_ID;
##Flask

1. Added the code with database information
2. Added GET method which gets everything from the database and returns it.
3. Added POST method where user can add information in the database using curl.

##Bottle

1. Added GET, DELETE.




##CURL Method

1. FOR POST... curl -H "Content-Type: application/json" -X POST -d @todo.json http://127.0.0.1:5000/todo
2. FOR DELETE... curl -X DELETE http://127.0.0.1:5000/todo/9
3. FOR UPDATE... curl -H "Content-Type: application/json" -X PUT -d @todo.json http://127.0.0.1:5000/todo/10
4. FOR GET... curl -X GET http://127.0.0.1:5000/todo/14

##uWSGI

1. Have made two .ini files which run each app individually.
2. uwsgi me.ini
3. uwsgi bottle.ini

#uWSGI Emperor mode

1. Both API's can run at the same time using Emperor mode.
2. Made a vassals folder containing both configuration files for the API's(.ini)
3. uwsgi --emperor vassals --uid http --gid http --master
