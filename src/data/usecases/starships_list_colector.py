from typing import List, Dict, Type
from src.infra import SwapiApiConsumer
from src.domain.usecases.starships_list_colector import StarshipsListColectiorInterface


class StarshipsListColectior(StarshipsListColectiorInterface):
    """ StarshipsListColector usecase """

    def __init__(self, api_consumer: Type[SwapiApiConsumer]) -> None:
        self.__api_consumer = api_consumer

    def list(self, page: int) -> List[Dict]:
        respnse = self.__api_consumer.get_starships(page)
        print(respnse)

