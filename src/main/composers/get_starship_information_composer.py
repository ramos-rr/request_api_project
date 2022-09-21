"""
COMPOSERS: Put every pieces together
"""
from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usecases.starship_information_colector import StarshipInformationCollector
from src.presenters.controllers.starships_id_colector_controller import StarshipInformationColectorController


def get_starship_information_composer():
    """Composer"""

    infra = SwapiApiConsumer()
    usecase = StarshipInformationCollector(infra)
    controller = StarshipInformationColectorController(usecase)

    return controller
