import json
from typing import List, Dict, Type
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.domain.usecases.starship_information_colector import StarshipInformationCollectorInterface


class StarshipInformationCollector(StarshipInformationCollectorInterface):
    """ Starship Information Colector usecase """

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def inform(self, starship_id: int) -> List[Dict]:
        api_response = self.__api_consumer.get_starship_information(starship_id)
        return self.__format_api_response(api_response.response, starship_id)

    @classmethod
    def __format_api_response(cls, informations: Dict, starship_id) -> List[Dict]:
        return [
            {
                "id": starship_id,
                "name": informations["name"],
                "model": informations["model"],
                "max_atmosphering_speed": informations["max_atmosphering_speed"],
                "hyperdrive_rating": informations['hyperdrive_rating'],
                "MGLT": informations['MGLT'],
            }]
