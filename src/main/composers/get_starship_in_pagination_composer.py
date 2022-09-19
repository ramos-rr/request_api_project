"""
COMPOSERS: Put every pieces together
"""
from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.data.usecases.starships_list_colector import StarshipsListColectior
from src.presenters.controllers.starships_list_colector_controller import StarshipsListColectoController


def get_starships_in_pagination_composer():
    """Composer"""

    infra = SwapiApiConsumer()
    usecase = StarshipsListColectior(infra)
    controller = StarshipsListColectoController(usecase)

    return controller
