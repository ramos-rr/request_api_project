from .starships_list_colector import StarshipsListColectior
from src.infra.swapi_api_consumer import SwapiApiConsumer


def test_list():
    """ testing list()"""
    api_consumer = SwapiApiConsumer()
    starships_list_colector = StarshipsListColectior(api_consumer)
    page = 1
    response = starships_list_colector.list(page)
    # assert api_consumer.get_starships_atributes == {"page": page}
    assert isinstance(response, list)
    assert isinstance(response[0], dict)
