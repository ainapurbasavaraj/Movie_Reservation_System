from reservationService.dbinterface.fetchtabledetails import FetchTableDetails
from reservationService.dbinterface.db_client import DbClient

class BuildMaker:

    def __init__(self, builder) -> None:
        self.builder=builder
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

    def BuildSqlSearchByTheatre(self,locationID="1"):
        self.common_operations('theatres')
        self.builder.select("t.theaterid,t.theatrename,t.theatretype,t.address,m.moviename,m.movieid,s.show_id,s.showdate,s.showtime,st.available_seats,st.amount,st.currency")
        self.builder.fromq("theatre_table t")
        self.builder.join("show_details s")
        self.builder.ON("t.theaterid")
        self.builder.IN(f"(select theaterid from theatre_table where locationid='{locationID}')")
        self.builder.AND("t.theaterid=s.theaterid")
        self.builder.join("movie_table m")
        self.builder.ON("m.movieid=s.movieid")
        self.builder.join("show_table st")
        self.builder.ON("s.show_id=st.show_id")
        print(f'self.builder.get_query() --> {self.builder.get_query()}')
        return self.builder.get_query()

    def BookMovie(self,book_movie_req):
        userid=book_movie_req.get('userid',None)
        showid=book_movie_req.get('showid',None)
        booked_seats=book_movie_req.get('NumberOfSeats',None)
        booking_id=book_movie_req.get('booking_id',None)
        self.builder.insert('booking_table')
        self.builder.values((booking_id,userid,showid,booked_seats,'PENDING'))
        return self.builder.get_query()

    def BuildCancelMovie(self):
        pass

    def RegisterUser(self,reg_data):
        userid=reg_data.get('userid',None)
        username=reg_data.get('username',None)
        emailid=reg_data.get('emailid',None)
        password=reg_data.get('password',None)
        phoneNumber=reg_data.get('phoneNumber',None)
        self.builder.insert('public.user_info')
        self.builder.values((userid,username,emailid,password,phoneNumber))
        return self.builder.get_query()



    def loginUser(self,loginData):
        userid=loginData.get('userid',None)
        password=loginData.get('password',None)
        self.builder.select('userid,password')
        self.builder.fromq('user_info')
        self.builder.where(f"userid='{userid}'")
        return self.builder.get_query()
    
    def insertToken(self,loginData,token,rf_timestamp):
        userid=loginData.get('userid',None)
        self.builder.insert("login_session")
        self.builder.values((userid,token,rf_timestamp))
        return self.builder.get_query()

    def updateToken(self,loginData,token,rf_timestamp):
        userid=loginData.get('userid',None)
        self.builder.update("login_session")
        self.builder.set(f"accetoken='{token}',refreshtime='{rf_timestamp}'")
        self.builder.where(f"userid='{userid}'")
        return self.builder.get_query()

    def updateAvailableSeats(self,bookingData,availableSeats):
        showid=bookingData.get('showid',None)
        self.builder.update("show_table")
        self.builder.set(f"available_seats='{availableSeats}'")
        self.builder.where(f"show_id='{showid}'")
        return self.builder.get_query()


    def logoutUser(self):
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
            ts=table.split('_')
            self.alias=ts[0][0]+ts[1][0]
            self.columns=self.get_columns(self.schema,table)
            columns=[]
            for col in self.columns:
                columns.append(self.alias+'.'+col[0])
            self.sql_attributes.update({table:columns})
        self.dbc.close_cursor()

    def fetchToken(self,uid):
        userid=uid
        self.builder.select("accetoken")
        self.builder.fromq(f"login_session")
        self.builder.where(f"userid='{userid}'")
        return self.builder.get_query()

    def deleteToken(self,uid):
        userid=uid
        self.builder.delete("login_session")
        self.builder.where(f"userid='{userid}'")
        return self.builder.get_query()

    def fetchSeatsAvailable(self,request):
        showid=request.get('showid',None)
        seats=request.get('NumberOfSeats',None)
        self.builder.select('available_seats')
        self.builder.fromq('show_table')
        self.builder.where(f"show_id='{showid}'")
        return self.builder.get_query()

    
    def bookMovieResponse(self,showid):
        self.builder.select('b.booking_id,b.payment_status,t.theatrename,t.theatretype,t.address,m.moviename,s.show_id,s.movieid,s.theaterid,s.showdate,s.showtime')
        self.builder.fromq('booking_table b')
        self.builder.join('show_details s')
        self.builder.ON(f"s.show_id='{showid}'")
        self.builder.join('theatre_table t')
        self.builder.ON('t.theaterid=s.theaterid')
        self.builder.join('movie_table m')
        self.builder.ON('m.movieid=s.movieid')
        return self.builder.get_query()

    def payment(self,booking_id,status):
        bookingId=booking_id
        self.builder.update("booking_table")
        self.builder.set(f"payment_status='{status}'")
        self.builder.where(f"booking_id='{bookingId}'")
        return self.builder.get_query()

    def getBookingDetails(self,userid):
        self.builder.select('b.booking_id,b.payment_status,b.show_id,s.theaterid,s.movieid,t.theatrename,t.theatretype,t.address,m.moviename,s.show_id,s.showdate,s.showtime,b.booked_seats,st.amount,st.currency')
        self.builder.fromq('booking_table b')
        self.builder.join('show_details s')
        self.builder.ON(f"b.userid='{userid}'")
        self.builder.AND("b.show_id = s.show_id")
        self.builder.join('theatre_table t')
        self.builder.ON('t.theaterid=s.theaterid')
        self.builder.join('movie_table m')
        self.builder.ON('m.movieid=s.movieid')
        self.builder.join('show_table st')
        self.builder.ON('st.show_id=b.show_id')
        return self.builder.get_query()


    def BookTicket(self,ticketing_data):
        bookingid=ticketing_data.get('booking_id',None)
        ticket_id=ticketing_data.get('ticket_id',None)
        ticket_url=ticketing_data.get('ticket_url',None)
        self.builder.insert('ticketing_table')
        self.builder.values((ticket_id,bookingid,ticket_url))
        return self.builder.get_query()

