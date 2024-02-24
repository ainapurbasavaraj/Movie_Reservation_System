
from actions.action import UsecaseAction
from usecase import usecase

class bookUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):

        action1 = UsecaseAction()
        action2 = UsecaseAction()
        action3 = UsecaseAction()

        self.set_start_action(action1)
        self.set_next_action(action1 , "OK", action2)
        self.set_next_action(action1 , "KO", action3)
        self.set_default_action(action3)