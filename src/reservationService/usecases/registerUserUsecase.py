from reservationService.usecases.actions.action import UsecaseAction
from reservationService.usecases.usecase import usecase
from reservationService.adapter.registerUserAdapter import RegisterUserAdapter,ValidateInputParams,CheckIfUserIDIsUnique

class RegisterUserUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):
        action1=ValidateInputParams(self.get_usecase_content())
        action2 = RegisterUserAdapter(self.get_usecase_content())
        action3 = UsecaseAction(self.get_usecase_content())
        self.set_start_action(action1)
        self.set_next_action(action1 , "SUCCESS", action2)
        self.set_default_action(action2)