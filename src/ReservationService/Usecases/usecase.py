
from Actions.Action import UsecaseAction

class usecase(object):

    def __init__(self) -> None:
        #Map of actions
        #ACTION1, SUCCESS, ACTION2
        #ACTION1, FAILURE, ACTION3
        self.actions_map = dict()
        self.start_action = None
        self.default_action = None
        self.register_actions()

    
    def set_next_action(self, action1, status, action2):
        destActionDict = self.actions_map.get(action1,None)
        if destActionDict:
            if destActionDict.get(status, None) is not None:
                raise Exception("Same status already registered for this action.")
            else:
                destActionDict[status] = action2
        else:
            self.actions_map[action1] = {status : action2}


    def set_start_action(self, action):
        self.start_action = action

    def set_default_action(self, action):
        self.default_action = action

    def register_actions(self):
        raise Exception("Not implemented action!!")

    def get_next_action(self,next_action, status):
        return self.actions_map.get(next_action)[status]

    def run(self):
        next_action = self.start_action
        status = next_action.execute()
        while(True):
            next_action = self.get_next_action(next_action, status)
            next_action = self.actions_map.get(next_action, self.default_action)
            if next_action is self.default_action:
                self.default_action.execute()
                break
            else:
                status = next_action.execute()
                



class searchUsecase(usecase):

    def __init__(self) -> None:
        super().__init__()

    def register_actions(self):

        action1 = UsecaseAction()
        action2 = UsecaseAction()
        action3 = UsecaseAction()

        self.set_start_action(action1)
        self.set_next_action(action1 , "SUCCESS", action2)
        self.set_next_action(action1 , "FAILURE", action3)
        self.set_default_action(action3)