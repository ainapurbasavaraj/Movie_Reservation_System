import psycopg2

class DbClient:
    def __init__(self) -> None:
        self.dbName='postgres'
        self.user='postgres'
        self.password='welcome'
        self.result=None
        self.cur,self.conn=self.get_cursor()

    def get_cursor(self):
        conn=psycopg2.connect(f'dbname={self.dbName} user={self.user} password={self.password}')
        cur=conn.cursor()
        return cur,conn

    def execute(self,request):
        try:
            self.cur.execute(request)
            print(f'The sql statement to be executed is {request}')
        except:
            print(f'exception occured')
            self.result='FAILURE'
            return
        if 'update' not in request and request.find('insert')==-1:
            self.result=self.cur.fetchall()
            print(f'self.result --> {self.result}')
            return self.result
            print(f'inside if condition --> {request}')
        
        self.conn.commit()
        self.result="SUCCESS"
        

    def get_columns(self,table_schema, table_name):

        """
        Creates and returns a list of dictionaries for the specified
        schema.table in the database connected to.
        """

        where_dict = {"table_schema": table_schema, "table_name": table_name}

        # cursor = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)

        self.cur.execute("""SELECT column_name, ordinal_position, is_nullable, data_type, character_maximum_length
                        FROM information_schema.columns
                        WHERE table_schema = %(table_schema)s
                        AND table_name   = %(table_name)s
                        ORDER BY ordinal_position""",
                        where_dict)
        # print(f'self.cur.fetchall() --> {self.cur.fetchall()}')
        self.result=self.cur.fetchall()
        

    def close_cursor(self):
        self.cur.close()

        

    def get_result(self):
        # print(f'inside get_result --> {self.result}')
        return self.result
