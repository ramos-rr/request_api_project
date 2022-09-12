from .starships_list_colector import StarshipsListColectior
from src.infra import SwapiApiConsumer


def test_list():
    api_consumer = SwapiApiConsumer()
    starships_list_colector = StarshipsListColectior(api_consumer)

    page = 1
    starships_list_colector.list(page)