import sqlite3
import pandas as pd

try:
    conn=sqlite3.connect(r"epfl.db")
    df=pd.read_sql("SELECT * FROM product", conn)
    print(df)
    conn.close()
except Exception as ex:
    print(ex)
