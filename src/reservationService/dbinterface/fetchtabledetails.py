class FetchTableDetails:
    def __init__(self,endpoint) -> None:
        self.endpoint=endpoint
        self.endpoints=[
            'location',
            'movies',
            'theatres',
            'bookticket',
            'getBookingDetails',
            'getTicketingDetails',
            'payment',
            'register',
            'login',
            'logout']
        self.result=self.__endpoint_to_table_mappings(endpoint)

    def __endpoint_to_table_mappings(self,ep):
        tables=[]
        common_tables=['movie_table','theatre_table','show_details']
        if ep not in self.endpoints:
            return None
        if ep=='location':
            tables.append('location_table')
        if ep=='movies' or ep=='theatres':
            common_tables.append('show_table')
            tables=common_tables
        if ep=='bookticket' or ep=='getBookingDetails':
            common_tables.append('booking_table')
            tables=common_tables
        if ep=='bookticket':
            common_tables.append('booking_table')
            common_tables.append('show_table')
            common_tables.append('ticketing_table')
            tables=common_tables
        if ep=='getTicketingDetails':
            tables.append('ticketing_table')
            tables.append('booking_table')
        if ep=='payment':
            tables.append('booking_table')
        if ep=='register':
            tables.append('user_info')
        if ep=='login' or ep=='logout':
            tables.append('login_session')
        
        return tables

    def get_table_mappings(self):
        return self.result


