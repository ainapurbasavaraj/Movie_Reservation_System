from reservationService.usecases.actions.action import UsecaseAction
from reservationService.usecases.usecase import usecase
from reservationService.adapter.loginAdapter import ValidateInputParams,GenerateToken

class LoginUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):

        # action1 = RegisterUserAdapter(self.get_usecase_content())
        action1=ValidateInputParams(self.get_usecase_content())
        # action2=CheckIfUserIDIsUnique(self.get_usecase_content())
        action2 = GenerateToken(self.get_usecase_content())
        #action2 = UsecaseAction(self.get_usecase_content())

        self.set_start_action(action1)

        self.set_next_action(action1 , "SUCCESS", action2)
        # self.set_next_action(action2 , "SUCCESS", action3)
        self.set_next_action(action2 , "SUCCESS", None)
        # self.set_default_action(action3)
        self.set_default_action(action2)