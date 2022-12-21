import pyodbc

class Database:
    def __init__(self):
        driver = 'DRIVER={SQL Server}'
        server = 'SERVER=192.168.0.231'
        port = 'PORT=3306'
        db = 'DATABASE=user10'
        user = 'UID=user10'
        pw = 'PWD=90513'
        conn_str = ';'.join([driver, server, port, db, user, pw])
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()
        """
        cursor.execute('select * from Employee')
        for row in cursor.fetchall():
            print(row)
        """

    def get_his(self):
        cursor = self.conn.execute('select * from History')
        his = cursor.fetchall()
        cursor.close()
        return(his)
    def get_emp(self):
        cursor = self.conn.execute('select * from Employee')
        emps = cursor.fetchall()
        cursor.close()
        return(emps)
    def get_clnt(self):
        cursor = self.conn.execute('select * from Client')
        clnt = cursor.fetchall()
        cursor.close()
        return(clnt)
    def get_ord(self):
        cursor = self.conn.execute('select * from orders')
        ord = cursor.fetchall()
        cursor.close()
        return(ord)
    def get_serv(self):
        cursor = self.conn.execute('select * from Services')
        serv = cursor.fetchall()
        cursor.close()
        return(serv)
    def get_pos(self):
        cursor = self.conn.execute('select * from Position')
        pos = cursor.fetchall()
        cursor.close()
        return(pos)

    def check_login(self):
        log = []
        self.cursor.execute(f"""SELECT login FROM Employee""")
        rows = self.cursor.fetchall()
        for i in rows:
            for j in i:
                log.append(j)
        return log

    def get_log(self, login):
        log = []
        self.cursor.execute(f"""SELECT password, PosID FROM Employee WHERE login = '{login}'""")
        rows = self.cursor.fetchall()
        for i in rows:
            for j in i:
                log.append(j)
        return log

    def add_ord(self, barcode, Date_create, Time_ordered, close_date, rental_time,
                       Client_ID, StatusID):
        cursor = self.conn.cursor()
        cursor.execute(
            f"INSERT INTO orders"
            f"(`barcode`, `Date_create`, `Time_ordered`, `close_date`, `rental_time`, `emp_id`, `Client_ID`, `StatusID`)"
            f"VALUES ('{barcode}', '{Date_create}', '{Time_ordered}', '{close_date}', '{rental_time}', '{Client_ID}', '{StatusID}')"
        )
        cursor.close()
        self.conn.commit()


if __name__ == '__main__':
    D = Database()
    D.get_emp()