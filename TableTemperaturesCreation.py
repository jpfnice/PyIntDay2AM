
import sqlite3

try:

    conn=sqlite3.connect(r"epfl.db")
   
    cursor=conn.cursor()
   
    cursor.execute("drop table temperatures")
    cursor.execute("create table temperatures (city varchar(20), time time, date date, temp float)")
    
    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)