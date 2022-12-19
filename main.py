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
    def get_emp(self):
        self.cursor.execute('select * from Employee')
        emps = self.cursor.fetchall()
        self.cursor.close()
        return(emps)
    def get_clnt(self):
        self.cursor.execute('select * from Client')
        clnt = self.cursor.fetchall()
        self.cursor.close()
        return(clnt)
    def get_ord(self):
        self.cursor.execute('select * from orders')
        ord = self.cursor.fetchall()
        self.cursor.close()
        return(ord)
    def get_serv(self):
        self.cursor.execute('select * from Services')
        serv = self.cursor.fetchall()
        self.cursor.close()
        return(serv)
    def get_pos(self):
        self.cursor.execute('select * from Position')
        pos = self.cursor.fetchall()
        self.cursor.close()
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


if __name__ == '__main__':
    D = Database()
    D.get_emp()