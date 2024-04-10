
from reservationService.usecases.actions.action import UsecaseAction

class usecase(object):

    def __init__(self, content) -> None:
        #Map of actions
        #ACTION1, SUCCESS, ACTION2
        #ACTION1, FAILURE, ACTION3
        self.actions_map = dict()
        self.start_action = None
        self.default_action = None
        self.content = content
        self.register_actions()

    def get_usecase_content(self):
        return self.content

    def set_next_action(self, action1, status, action2):
        destActionDict = self.actions_map.get(action1,None)
        print(f'status --> {status},self.actions_map --> {self.actions_map}')
        if destActionDict:
            print(f'destActionDict --> {destActionDict}')
            if destActionDict.get(status, None) is not None:
                print(f'status --> {status}')
                raise Exception("Same status already registered for this action.")
            else:
                print(f'setting the {status} for action')
                destActionDict[status] = action2
        else:
            self.actions_map[action1] = {status : action2}


    def set_start_action(self, action):
        self.start_action = action

    def set_default_action(self, action):
        self.default_action = action

    def register_actions(self):
        raise Exception("Not implemented action!!")

    def get_next_action(self,current_action, status):
        
        return self.actions_map.get(current_action)[status]

    def run(self):
        next_action = self.start_action
        status = next_action.execute()
        while(True):
            next_action = self.get_next_action(next_action, status)
            if self.actions_map.get(next_action, self.default_action) is self.default_action:
                self.default_action.execute()
                break
            else:
                status = next_action.execute()
                



