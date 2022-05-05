
import sqlite3

try:

    with sqlite3.connect(r"epfl.db") as conn:
        cursor=conn.cursor()
        cursor.execute("drop table if exists temperatures")
        cursor.execute("create table temperatures (city varchar(20), time time, date date, temp float)")
        
        cursor.close()

except Exception as ex:
    print(ex)