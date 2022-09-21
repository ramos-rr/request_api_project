from abc import ABC, abstractmethod
from typing import Tuple, Dict, Type
from requests import Request


class SwapiApiConsumerInterface(ABC):

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """ Interface for API and Usercases"""
        raise NotImplementedError

    @abstractmethod
    def get_starship_information(self, starship_id: int) -> Dict:
        """ Method for API Usercase """
        raise NotImplementedError
