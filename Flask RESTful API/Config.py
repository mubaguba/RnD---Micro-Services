#All of this is for the location of the database file.
import os
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'Practice.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
print (basedir) #Prints the path.