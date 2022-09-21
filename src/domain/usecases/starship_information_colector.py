from abc import ABC, abstractmethod
from typing import Dict, List


class StarshipInformationCollectorInterface(ABC):
    """ Starship Information Colectior Interface"""

    @abstractmethod
    def inform(self, starship_id: int) -> Dict:
        """ Must implement"""
        raise Exception('Must implement list method')