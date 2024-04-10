from src.reservationService.Db_operations.builder import Builder

class SqlBuilderConcrete(Builder):
    def __init__(self) -> None:
        super().__init__()
        self.result=''

    def select(self):
        pass

    def fromq(self):
        pass

    def where(self):
        pass

    def innerjoin(self):
        pass

    def outerjoin(self):
        pass

    def insert(self):
        pass

    def update(self):
        pass

    def build(self)
        pass

    def get_query(self):
        return self.result