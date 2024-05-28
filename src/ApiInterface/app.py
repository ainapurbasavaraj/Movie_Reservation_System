from flask import Flask, jsonify, request
#from flask_restful import Resource
import json
import os
#from reservationService.search.searchByLocationService import SearchByLocationService
from reservationService.usecases import searchUsecase
from reservationService.search import searchByLocationService,searchByMovieService,searchByTheatreService

app = Flask(__name__)


@app.route("/reservationService/location")
def get_location():


    #Return dict of location id and names
    #{
	# 	locations: [{
	# 	    	locationid : string,
	# 		locationname : string,
	# 	}]
	# }
	location_service_obj=searchByLocationService.SearchByLocationService()
	locations=location_service_obj.execute(request)
	if locations:
		return locations
	else:
		return 'The locations are temporarily unavailable'


@app.route("/reservationService/movies/<string:locationId>")
def search_movies_by_location(locationId):

    # {
	# 	movies: [{
	# 		movieId : string,
	# 		moviename : string,
	# 		theatres : [{
	# 			theatreid : string,
	# 			theatrename : string,
	# 			theatretype : [PVR, IMAX, INOX]
	# 			Address : string,
	# 			available slots : [showdetails],
	# 			price : price
	# 		}],
			
	# 	}]
	# }
	movie_obj=searchByMovieService.SearchByMovieService()
	list_of_movies=movie_obj.execute(locationId)

	return '{"Movies" : "%s"}' %(list_of_movies)


@app.route("/reservationService/theatres/<string:locationId>")
def search_theatres_by_location(locationId):

    # {
	# 	theatres: [{
	# 		theatreid : string,
	# 		theatreName : string,
	# 		theatretype : [PVR, IMAX, INOX],
	# 		Address : string,
	# 		movies : [{
	# 			movieName : string,
	# 			movieId : string,
	# 			available slots : [showdetails],
	# 			price : price
	# 		}],
			
	# 	}]
	# }

    return "theatres"


@app.route("/reservationService/bookticket", methods=['POST'])
def book_ticket():
    #Decode body
    # {
	# 	location : string,
	# 	theatreId : string,
	# 	movieId : string,
	# 	available slot : [showdetails],
           
	# }

    #resoponse:
    # {
	# 	booking detail : {
	# 	status : string,
	# 	bookingid : string,
	# 	theatreName : string,
	# 	theatretype : [PVR, IMAX, INOX],
	# 	Address : string,
	# 	moviename : string,
	# 	showdetails : showdetails,
	# 	bookingAmount : price,
	# 	}
	# }

    return "booking details"

from flask import abort

@app.before_request
def valid_bookingId():
    print(request.query_string)
    if "getBookingDetails" == request.endpoint:
        if b'bookingId' not in request.query_string:
            print("booking id not found")
            abort(404)
    


#@app.route("/reservationService/getBookingDetails?userid=<string:userId>")
@app.route("/reservationService/getBookingDetails")
def getBookingDetails():

    #return "all booling details of user"
    return request.query_string

#@app.route("/reservationService/getBookingDetail?userid=<string:userId>&bookingid=<string:bookingId>")
@app.route("/reservationService/getBookingDetail")
def getBookingDetail():

    return request.query_string



@app.route("/reservationService/payment", methods=['POST'])
def payment():

    return "Payment status"



@app.route("/reservationService/register", methods=['POST'])
def register():

    return "status"


@app.route("/reservationService/login", methods=['POST'])
def login():

    return "accesstoken"


@app.route("/reservationService/logout")
def logout():

    return "logout success"


@app.route("/reservationService/deregister")
def deregister():

    return "deregister success"

#@app.route("/store", methods=['POST'])


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5661)