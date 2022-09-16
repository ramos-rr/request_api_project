from src.domain.usecases.starships_list_colector import StarshipsListColectiorInterface
from typing import Type, Dict

class StarshipsListColectoController:

    def __init__(self, starship_list_colector: Type[StarshipsListColectiorInterface]) -> None:
        self.__use_case = starship_list_colector

    def handle(self, http_request: Dict):

        page = http_request[]