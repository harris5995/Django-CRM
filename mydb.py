#install Mysql on your computer
#mysql installer from website
#pip install mysql
#pip install mysql-connector
#pip install mysql-connector-python

import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'venomancer'

)

#prepare a cursor object
cursorObject = dataBase.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE harris")

print("All Done!")