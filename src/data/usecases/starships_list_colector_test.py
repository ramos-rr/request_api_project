from .starships_list_colector import StarshipsListCollector
from src.infra.swapi_api_consumer import SwapiApiConsumer
from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpy


def test_list_spy():
    """ testing list() with Spy"""
    api_consumer = SwapiApiConsumerSpy()
    starships_list_colector = StarshipsListCollector(api_consumer)
    page = 1
    response = starships_list_colector.list(page)
    assert api_consumer.get_starships_atributes == {"page": page}
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


# def test_list_online():
#     """ testing list() for real (online)"""
#     api_consumer = SwapiApiConsumer()
#     starships_list_colector = StarshipsListCollector(api_consumer)
#     page = 1
#     response = starships_list_colector.list(page)
#     assert isinstance(response, list)
#     assert isinstance(response[0], dict)
