from typing import List, Dict, Type
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.domain.usecases.starships_list_colector import StarshipsListColectiorInterface


class StarshipsListColectior(StarshipsListColectiorInterface):
    """ StarshipsListColector usecase """

    def __init__(self, api_consumer: Type[SwapiApiConsumerInterface]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        api_response = self.__api_consumer.get_starships(page)
        starships_formated_list = self.__format_api_response(api_response.response['results'])
        return starships_formated_list

    @classmethod
    def __format_api_response(cls, results: List[Dict]):
        starships_formated_list = list()

        for starship in results:
            starships_formated_list.append(
                {
                    "id": starship['url'].split('/')[-2],
                    "name": starship['name'],
                    "model": starship["model"],
                    "max_atmosphering_speed": starship["max_atmosphering_speed"],
                    "hyperdrive_rating": starship['hyperdrive_rating'],
                    "MGLT": starship['MGLT'],
                }
            )
        return starships_formated_list

