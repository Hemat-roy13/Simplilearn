import pandas as pd
import sqlite3

"""
Pandas with sqlite3, inbuilt python database
"""

createTable = """
Create table student 
(Id INTEGER, Name Varchar(20),Math REAL, Science REAL);
"""

executeSQL = sqlite3.connect(":memory:")
executeSQL.execute(createtable)
execute.commit()

SQL_query = executeSQL.execute("select * from student")
resultset = SQL_query.fetchall()

resultset

insert_record = [(10,'Jack',95,97), (29,'Tom',12,28)]
insert_stmt = "Insert into student values (?,?,?,?)"
exeuteSQL.execute(insert_stmt, insert_record)
exeuteSQL.commit()

SQL_query = executeSQl.execute("select * from student")

resultset = SQL_query.fetchall()
resultset

df_students_records = pd.DataFrmae(resultset,columns=zip(*SQL_query.description)[0])
df_students_records

df = pd.DataFrame(SQL_query.fetchall())
