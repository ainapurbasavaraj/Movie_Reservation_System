import psycopg2

class DbClient:
    def __init__(self,request) -> None:
        self.statement=request
        self.dbName='postgres'
        self.user='postgres'
        self.password='welcome'
        self.result=''

    def execute(self):
        conn=psycopg2.connect(f'dbname={self.dbName} user={self.user} password={self.password}')
        cur=conn.cursor()
        cur.execute(self.statement)
        self.result=cur.fetchall()

    def get_result(self):
        return self.result
