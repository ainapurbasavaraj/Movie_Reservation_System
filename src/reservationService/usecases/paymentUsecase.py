from reservationService.usecases.actions.action import UsecaseAction
from reservationService.usecases.usecase import usecase
from reservationService.adapter.paymentAdapter import updatePayment,GenerateTicketingID
from reservationService.adapter.tokenAuthAdapter import TokenAuth

class PaymentUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):
        action1=TokenAuth(self.get_usecase_content())
        action2 = updatePayment(self.get_usecase_content())
        action3=GenerateTicketingID(self.get_usecase_content())
        self.set_start_action(action1)
        self.set_next_action(action1 , "SUCCESS", action2)
        self.set_next_action(action2 , "SUCCESS", action3)
        self.set_next_action(action3 , "SUCCESS", None)
        self.set_default_action(action3)