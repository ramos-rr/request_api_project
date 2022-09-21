from src.domain.usecases.starship_information_colector import StarshipInformationCollectorInterface
from typing import Type, Dict


class StarshipInformationColectorController:
    """ Controler to get a Starshi information"""

    def __init__(self, starship_information_colector: Type[StarshipInformationCollectorInterface]) -> None:
        self.__use_case = starship_information_colector  # Indicate WHO IS THE USECASE FOR THIS CLASS

    # DEINE A METHOD THAT WILL RECIEVE THOSE QUERY_PARAMS FROM PAGE TO SEND TO USECASE
    def handle_starshp_info_parameter(self, http_request: Dict) -> Dict:
        """
        Method that recieves a validated http and call USECASE to get the information desided.
        :param http_request: Http request already validated and checked
        :return: Starship information data, as desired
        """
        # EXTRAC: TRANSFORM A STRING QUERRY PARAM TO INTEGER
        starship_id = http_request["body"]["starship_id"]
        # USE: USES THE PARAMETER COLECTED
        starship_info = self.__use_case.inform(starship_id=starship_id)
        # FORMAT: SETS THE DATA TO A DESIRED PATTERN
        http_response = {"status_code": 200, "data": starship_info}

        return http_response
