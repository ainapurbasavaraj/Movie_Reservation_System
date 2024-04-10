
from dataclasses import dataclass

from enum import Enum
class TheatreType(Enum):
    PVR=1
    IMAX=2
    INOX=3

@dataclass
class Price:
    amount: int
    currency: str

@dataclass
class Location:
    id: str
    name: str
    
@dataclass
class ShowDetails:
    showDate: str
    showTime: str
    # seatNumbers: list(int)
    seatNumbers: list()

@dataclass
class Theatre:
    theatreId: str
    theatreName: str
    theatreType: TheatreType
    address: str
    # availableSlots: list(ShowDetails)
    availableSlots: list()
    price: Price

@dataclass
class Movie:

    movieId: str
    movieName: str
    #theatres: list(Theatre)
    theatres: list()

@dataclass
class BookingDetails:
    status : str
    bookingId : str
    theatreName : str
    theatreType : TheatreType
    address : str
    movieName : str
    showDetails : ShowDetails
    bookingAmount : Price

@dataclass
class PaymentDetails:
	cardNumber : str
	name : str
	cvv : str


@dataclass
class RegistrationDetails:
    userId : str
    name : str
    password : str
    emailid : str
    phoneNumber : str

@dataclass
class LoginDetails:
    userId : str
    password : str