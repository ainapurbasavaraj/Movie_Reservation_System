
from reservationService.adapter.getLocationAdapter import GetLocationAdapter
class SearchByLocationUsecaseAction:

    def __init__(self, content) -> None:
        self.usecase_content = content

    def get_usecase_content(self):
        return self.usecase_content

    def execute(self):
        self.get_usecase_content().set_locations(GetLocationAdapter().execute())
        print(f'inside SearchByLocationUsecaseAction -->self.get_usecase_content() ---> {self.get_usecase_content().get_locations()}')
        return "SUCCESS"
