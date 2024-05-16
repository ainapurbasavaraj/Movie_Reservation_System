# from crypt import methods
from email import header
from flask import Flask, jsonify, request
#from flask_restful import Resource
import json
import os
#from reservationService.search.searchByLocationService import SearchByLocationService
from reservationService.usecases import searchUsecase
from reservationService.search import searchByLocationService,searchByMovieService,searchByTheatreService
from reservationService.register import registerUserService,loginService,logoutUserService
from reservationService.book import bookTicketService,paymentService,getbookingDetailsService

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


# @app.route("/reservationService/movies/<string:locationId>")
@app.route("/reservationService/movies/")
def search_movies_by_location():
	locationId=request.args.get('locationid')

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


# @app.route("/reservationService/theatres?locationid=<string:locationId>")
@app.route("/reservationService/theatres/")
def search_theatres_by_location():
	locationid=request.args.get('locationid')
	print('inside search_theatres_by_location')

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
	theatre_obj=searchByTheatreService.SearchByTheatreService()
	list_of_theatres=theatre_obj.execute(locationid)

	return '{"theatres" : "%s"}' %(list_of_theatres)




@app.route("/reservationService/bookticket", methods=['POST'])
def book_ticket():
	book_movie_obj=bookTicketService.BookTicketService()
	return book_movie_obj.execute(request)
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

from flask import abort

# @app.before_request
# def valid_bookingId():
#     print(request.query_string)
#     if "getBookingDetails" == request.endpoint:
#         if b'bookingId' not in request.query_string:
#             print("booking id not found")
#             abort(404)
    


#@app.route("/reservationService/getBookingDetails?userid=<string:userId>")
@app.route("/reservationService/getBookingDetails")
def getBookingDetails():
	params=dict()
	userId=request.args.get('userId')
	token=request.headers.get('Authorization')
	params.update({
		'userid':userId,
		'token':token
	})
	gbd=getbookingDetailsService.GetBookingDetailService()
	return gbd.execute(params)


#@app.route("/reservationService/getBookingDetail?userid=<string:userId>&bookingid=<string:bookingId>")
@app.route("/reservationService/getBookingDetail")
def getBookingDetail():

    return request.query_string



@app.route("/reservationService/payment", methods=['POST'])
def payment():

	reg_user_obj=paymentService.paymentService()

	return reg_user_obj.execute(request)



@app.route("/reservationService/register", methods=['POST'])
def register():

	reg_user_obj=registerUserService.RegisterUserService()

	return reg_user_obj.execute(request)


@app.route("/reservationService/login", methods=['POST'])
def login():

	login_obj=loginService.LoginService()
	return login_obj.execute(request)


@app.route("/reservationService/logout",methods=['DELETE'])
def logout():
	#fetch the header having bearer token and payload having the userid
	logout_obj=logoutUserService.LogoutService()
	return logout_obj.execute(request)


@app.route("/reservationService/deregister")
def deregister():

    return "deregister success"

#@app.route("/store", methods=['POST'])


if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 5661)