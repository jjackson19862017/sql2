import os
import datetime
import pymysql

# Get username from Cloud9 Workspace
# Modify this variable if runnin on another enviroment

username = os.getenv('C9_USER')

# Connect to Database
connection = pymysql.connect(host='localhost',
                             user=username,
                             password='',
                             db='Chinook')

try:
    # Run a Query
    with connection.cursor() as cursor:
        rows = [("Bob", 21, "1990-02-06 23:04:56"),
                ("Jim", 56, "1955-05-09 13:12:45"),
                ("Fred", 100, "1911-04-05 14:15:16")]
        cursor.executemany("INSERT INTO Friends Values (%s, %s, %s);", rows)
        cursor.execute("""Create Table if not exists
                       Friends(name char(20), age int, DOB datetime);""")
        # Not that the above will still display a warning (Not Error) if 
        # the table already exists
        connection.commit()
finally:
    # Close the connection, Regardless of wether the above was successful
    connection.close()
