from src.reservationService.dbinterface.builder import Builder

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

    def insert(self,values):
        pass

    def update(self,tables):
        pass

    def build(self):
        pass

    def join(self):
        pass

    def on(self):
        pass

    def IN(self):
        pass

    def AND(self):
        pass

    def values(self):
        pass

    def set(self):
        pass

    def get_query(self):
        return self.result+';'