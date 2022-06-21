import sqlite3

try:
    # Step 1: connection
    conn=sqlite3.connect("epflBis.db")
    # Step 2: create a cursor object
    cursor=conn.cursor()
    # Step 3: using the cursor, execute SQL statements:
    cursor.execute("drop table if exists temperatures")   
    cursor.execute("create table temperatures (city varchar(20), ctime time, cdate date, temp float)")
    # cursor.execute("select * from temperatures")
    
    # while True:
    #     row = cursor.fetchone()
    #     if row == None:
    #         break
    #     print(row)
    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)