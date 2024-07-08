
from reservationService.usecases.actions.action import UsecaseAction
from reservationService.usecases.actions.searchByLocationAction import SearchByLocationUsecaseAction
from reservationService.usecases.usecase import usecase
from reservationService.adapter.searchByMoveAdapter import SearchByMovieAdapter

class SearchByMovieUsecase(usecase):

    def __init__(self, content) -> None:
        super().__init__(content)

    def register_actions(self):

        action1 = SearchByMovieAdapter(self.get_usecase_content())
        action2 = UsecaseAction(self.get_usecase_content())
        self.set_start_action(action1)
        self.set_next_action(action1 , "SUCCESS", action2)
        self.set_default_action(action2)