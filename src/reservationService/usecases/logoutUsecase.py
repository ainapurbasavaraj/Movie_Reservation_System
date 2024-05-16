from reservationService.usecases.usecase import usecase
from reservationService.adapter.tokenAuthAdapter import TokenAuth
from reservationService.adapter.logoutAdapter import AuthenticateToken,DeleteToken
from reservationService.usecases.actions.action import UsecaseAction

class LogoutUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):

        # action1 = RegisterUserAdapter(self.get_usecase_content())
        # action1=AuthenticateToken(self.get_usecase_content())
        action1=TokenAuth(self.get_usecase_content())
        action2=DeleteToken(self.get_usecase_content())
        #action2 = GenerateToken(self.get_usecase_content())
        action3 = UsecaseAction(self.get_usecase_content())

        self.set_start_action(action1)

        self.set_next_action(action1 , "SUCCESS", action2)
        # self.set_next_action(action2 , "SUCCESS", action3)
        self.set_next_action(action2 , "SUCCESS", action3)
        # self.set_default_action(action3)
        self.set_default_action(action3)