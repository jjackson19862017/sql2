import os
import pymysql

# Get username from Cloud9 Workspace
# Modify this variable if runnin on another enviroment

username = os.getenv('C9_USER')

# Connect to Database
connection = pymysql.connect(host='localhost', user=username, password='', db='Chinook')

try:
    # Run a Query
    with connection.cursor() as cursor:
        sql = "Select * From Artist;"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    # Close the connection, Regardless of wether the above was successful
    connection.close()
