from src.domain.usecases.starships_list_colector import StarshipsListColectiorInterface
from typing import Type, Dict


class StarshipsListColectoController:
    """ Controler to list Starships"""

    def __init__(self, starship_list_colector: Type[StarshipsListColectiorInterface]) -> None:
        self.__use_case = starship_list_colector  # Indicate WHO IS THE USECASE FOR THIS CLASS

    # DEINE A METHOD THAT WILL RECIEVE THOSE QUERY_PARAMS FROM PAGE TO SEND TO USECASE
    def handle_page_parameter(self, http_request: Dict) -> Dict:
        """
        Method that recieves a validated http and call USECASE to get the information desided.
        :param http_request: Http request already validated and checked
        :return: Starship list, as desired
        """
        page = http_request["query_params"]["page"]
        starships_list = self.__use_case.list(page)
        http_response = {"status_code": 200, "data": starships_list}

        return http_response
