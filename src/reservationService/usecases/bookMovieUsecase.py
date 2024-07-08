from reservationService.usecases.actions.action import UsecaseAction
from reservationService.usecases.usecase import usecase
from reservationService.adapter.bookMovieAdapter import checkIfSeatsAvailable,GenerateBookingID,UpdateAvailableSeats,GenerateBookingResponse
from reservationService.adapter.tokenAuthAdapter import TokenAuth
#from reservationService.data.reservationLogger import ReservationLogger
from reservationService.Log import log

class BookMovieUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)
        # self.log=ReservationLogger.get_logger()

    def register_actions(self):
        log.info("register action started ..")
        action1=TokenAuth(self.get_usecase_content())
        action2 = checkIfSeatsAvailable(self.get_usecase_content())
        action3=GenerateBookingID(self.get_usecase_content())
        action4=UpdateAvailableSeats(self.get_usecase_content())
        action5=GenerateBookingResponse(self.get_usecase_content())
        self.set_start_action(action1)
        self.set_next_action(action1 , "SUCCESS", action2)
        self.set_next_action(action2 , "SUCCESS", action3)
        self.set_next_action(action3,'SUCCESS',action4)
        self.set_next_action(action4,'SUCCESS',action5)
        self.set_next_action(action5,'SUCCESS',None)
        self.set_default_action(action5)
        log.info("register action completed successfully ..")