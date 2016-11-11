# RnD---Micro-Services
Repository for all code to do with the project

1. The Bottle folder has code which Kevin has developed.
2. The Flask folder has code which Mubasher has developed.


##Flask

1. Added the code with database information
2. Added GET method which gets everything from the database and returns it.
3. Added POST method where user can add information in the database using curl.

##Bottle





##CURL Method

1. FOR POST... curl -H "Content-Type: application/json" -X POST -d @todo.json http://127.0.0.1:5000/
2. FOR DELETE... curl -X DELETE http://127.0.0.1:5000/del/1
3. FOR UPDATE... curl -H "Content-Type: application/json" -X PUT -d @todo.json http://127.0.0.1:5000/update/1
4. FOR GET... curl -X GET http://127.0.0.1:5000/