from .swapi_api_consumer import SwapiApiConsumer


def test_get_starship():
    """ Get response from API. """

    swapi_api_consumer = SwapiApiConsumer()
    page = 1

    get_starships_response = swapi_api_consumer.get_starships(page=page)

    assert get_starships_response.request.method == 'GET'  # See in the function inside class how it has been set
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'  # See in the function inside class
    # how it has been set
    assert get_starships_response.request.params == {'page': page}  # See in the function inside class how it has been
    # set
    assert get_starships_response.status_code == 200
    assert isinstance(get_starships_response.response['results'], list)

