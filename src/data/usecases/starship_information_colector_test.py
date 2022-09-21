from .starship_information_colector import StarshipInformationCollector
from src.infra.test.swapi_api_consumer import SwapiApiConsumerSpy
from src.infra.swapi_api_consumer import SwapiApiConsumer


def test_inform_spy():
    """ testing information page"""
    api_consumer = SwapiApiConsumerSpy()
    starship_information_colector = StarshipInformationCollector(api_consumer)
    starship_id = 64
    response = starship_information_colector.inform(starship_id)
    print(response)
    assert api_consumer.get_starship_info_atributes == {"starship_id": starship_id}
    assert isinstance(response, list)
    assert isinstance(response[0], dict)


# def test_inform_online():
#     """ testing information page"""
#     api_consumer = SwapiApiConsumer()
#     starship_information_colector = StarshipInformationCollector(api_consumer)
#     starship_id = 64
#     response = starship_information_colector.inform(starship_id)
#     print(response)
#     # assert api_consumer.get_starship_info_atributes == {"starship_id": starship_id}
#     assert isinstance(response, list)
#     assert isinstance(response[0], dict)
