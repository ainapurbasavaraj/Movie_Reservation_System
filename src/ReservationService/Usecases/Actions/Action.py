
class UsecaseAction:

    def __init__(self, content) -> None:
        self.usecase_content = content

    def get_usecase_content(self):
        return self.usecase_content

    def execute(self):
        print("Executing Actions...")
        return "SUCCESS"
