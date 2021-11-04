"""

create table product (name varchar(20) primary key, price float, qty int)
drop table product # to delete the whole table

insert into product values ('Prod1', 34.56, 23)
select * from product
select * from product where qty > 20
delete from product where qty=0
update product set price=price*1.25 where name='Prod3'

commit # validate a transaction
rollback # invalidate the transaction (the insert,delete,update done previously)

sql alchemy 

"""

import sqlite3

try:
    # Step 1: connection
    conn=sqlite3.connect(r"epfl.db")
    # Step 2: create a cursor object
    cursor=conn.cursor()
    # Step 3: using the cursor, execute SQL statements:
    cursor.execute("insert into product values ('prod600', 22.3, 34)")
    print(f"{cursor.rowcount} rows were returned")
    cursor.execute("commit") 
    
    cursor.execute("select * from product")
     
    while True:
        row = cursor.fetchone()
        if row == None:
            break
#         print("{}, {}, {}".format(row[0], row[1], row[2]))
        print(f"{row[0]}, {row[1]}, {row[2]}")
#     res=cursor.fetchall()    
#     print(res)
    print("{} rows were returned".format(cursor.rowcount))
      
    cursor.close()
    conn.close()
except Exception as ex:
    print(ex)