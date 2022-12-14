import pyodbc


driver = 'DRIVER={SQL Server}'
server = 'SERVER=192.168.0.122'
port = 'PORT=3306'
db = 'DATABASE=user10'
user = 'UID=user10'
pw = 'PWD=90513'
conn_str = ';'.join([driver, server, port, db, user, pw])

conn = pyodbc.connect(conn_str)
cursor = conn.cursor()
cursor.execute('select * from emp')
for row in cursor.fetchall():
    print (row)