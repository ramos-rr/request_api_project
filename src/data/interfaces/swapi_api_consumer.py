from abc import ABC, abstractmethod
from typing import Tuple, Dict, Type
from requests import Request


class SwapiApiConsumerInterface(ABC):

    @abstractmethod
    def get_starships(self, page: int) -> Tuple[int, Type[Request], Dict]:
        """ Interface for API and Usercases"""
        raise NotImplementedError