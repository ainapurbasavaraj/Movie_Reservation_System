from reservationService.dbinterface.fetchtabledetails import FetchTableDetails
from reservationService.dbinterface.db_client import DbClient

class BuildMaker:

    def __init__(self, builder) -> None:
        self.builder=builder
    # def __init__(self) -> None:
        self.tables=[]
        self.columns=[]
        self.alias=''
        self.sql_attributes=dict()
        self.dbc=DbClient()
        self.schema='public'

    def Build_sql_searchByLocation(self):
        #get the tables required for response construction
        self.common_operations('getBookingDetails')
        #query the schema and find the relevant columns and assign a alias
        # print(self.sql_attributes)
        self.builder.select('l.locationid,l.locationname')
        self.builder.fromq('location_table l')
        return self.builder.get_query()

    def BuildSqlSearchByMovie(self,locationID="1"):

        self.common_operations('movies')
        self.builder.select("m.movieid,m.moviename,s.theaterid,t.theatrename,t.theatretype,t.address,s.show_id,s.showdate,s.showtime,st.available_seats,st.amount,st.currency")
        self.builder.fromq("movie_table m")
        self.builder.join("show_details s")
        self.builder.ON("m.movieid")
        self.builder.IN(f"(select movieid from movie_table where locationid='{locationID}')")
        self.builder.AND("s.movieid=m.movieid")
        self.builder.join("theatre_table t")
        self.builder.ON("t.theaterid=s.theaterid")
        self.builder.join("show_table st")
        self.builder.ON("s.show_id=st.show_id")
        return self.builder.get_query()

    def BuildSqlSearchByTheatre():
        pass

    def BuildSqlBookMovie():
        pass

    def BuildCancelMovie():
        pass

    def find_tables(self,endpoint):
        ft=FetchTableDetails(endpoint)
        self.tables=ft.get_table_mappings()

    def get_schema(self,table):
        sql_command=f"\d {table};"
        schema=DbClient(sql_command)
        return schema.get_result()

    def get_columns(self,schema,table):
        self.dbc.get_columns(schema,table)
        return self.dbc.get_result()


    def common_operations(self,endpoint):
        #find tables
        self.find_tables(endpoint)
        for table in self.tables:
            self.alias=''
            self.columns=[]
            # schema=self.get_schema(table)
            # # print(f'schema --> {schema}')
            ts=table.split('_')
            self.alias=ts[0][0]+ts[1][0]
            self.columns=self.get_columns(self.schema,table)
            columns=[]
            for col in self.columns:
                columns.append(self.alias+'.'+col[0])
            self.sql_attributes.update({table:columns})
        self.dbc.close_cursor()

# if __name__=='__main__':
#     b=BuildMaker()
#     b.BuildSqlSearchByMovie()

