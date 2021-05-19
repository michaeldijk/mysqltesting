import os
import pymysql


#Get username from system
#(modify this variable if running it on another environment)
username = os.getenv("C9_USER")


#Connect to the database
connection = pymysql.connect(host="localhost", user=username, password="", db="Chinook")
try:
    #run a query
    with connection.cursor() as cursor:
        sql = "select * from Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    #close connection, regardless of whether the above was succesful
    connection.close()
