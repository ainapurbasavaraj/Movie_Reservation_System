from reservationService.dbinterface.builder import Builder

class SqlBuilder(Builder):
    def __init__(self) -> None:
        super().__init__()
        self.result=''

    def select(self,columns):
        if not self.result:
            self.result=f"select {columns}"

    def fromq(self,tables):
        if self.result:
            self.result+=f' FROM {tables}'

    def where(self,conditions):
        if self.result:
            self.result+=f' WHERE {conditions}'

    def innerjoin(self):
        pass

    def outerjoin(self):
        pass

    def insert(self,table):
        if not self.result:
            self.insert=f'insert into {table}'

    def update(self,tables):
        pass

    def build(self):
        pass

    def join(self,table):
        if self.result:
            self.result+=f' join {table}'

    def ON(self,condition):
        if self.result:
            self.result+=f' ON {condition}'

    def IN(self,condition):
        if self.result:
            self.result+=f' IN {condition}'

    def AND(self,condition):
        if self.result:
            self.result+=f' AND {condition}'

    def values(self,values):
        if self.result:
            self.result+=f' ({values})'

    def set(self):
        pass

    def get_query(self):
        return self.result+';'