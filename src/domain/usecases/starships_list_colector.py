from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipsListColectiorInterface(ABC):
    """ Starships Colectior Interface"""

    @abstractmethod
    def list(self, page: int) -> List[Dict]:
        """ Must implement"""
        raise Exception('Must implement list method')