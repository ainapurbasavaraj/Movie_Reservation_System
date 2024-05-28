class BuildMaker:

    def __init__(self,builder) -> None:
        self.builder=builder()

    def Build_sql_searchByLocation(self):
        self.builder.select('locatonid,locationmame')
        self.builder.fromq('LOCATION_TABLE')
        return self.builder.get_query()

    def BuildSqlSearchByMovie():
        pass

    def BuildSqlSearchByTheatre():
        pass

    def BuildSqlBookMovie():
        pass

    def BuildCancelMovie():
        pass