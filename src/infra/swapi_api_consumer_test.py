from .swapi_api_consumer import SwapiApiConsumer


def test_get_starship(requests_mock):
    """ Get response from API. """
    requests_mock.get('https://swapi.dev/api/starships/', status_code=200, json={'some': "thing"})
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starships(page=1)

    print(response)
