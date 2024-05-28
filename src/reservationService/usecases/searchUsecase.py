
from reservationService.usecases.actions.action import UsecaseAction
from reservationService.usecases.usecase import usecase

class searchUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):

        action1 = UsecaseAction(self.get_usecase_content())
        action2 = UsecaseAction(self.get_usecase_content())
        action3 = UsecaseAction(self.get_usecase_content())

        self.set_start_action(action1)
        self.set_next_action(action1 , "SUCCESS", action2)
        self.set_next_action(action1 , "FAILURE", action3)
        self.set_default_action(action3)