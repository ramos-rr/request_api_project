import pytest
from .swapi_api_consumer import SwapiApiConsumer
from src.errors import HttpRequestErrors


def test_get_starship(requests_mock):
    """ Get response from API. """
    # Mock set up
    status_code_mock = 200
    requests_mock.get('https://swapi.dev/api/starships/', status_code=status_code_mock, json={'helo': 'world', 'results': [{}]})

    # Main test instance
    swapi_api_consumer = SwapiApiConsumer()
    page = 1

    # Principal API command
    get_starships_response = swapi_api_consumer.get_starships(page=page)

    # Assertions
    assert get_starships_response.request.method == 'GET'  # See in the function inside class how it has been set
    assert get_starships_response.request.url == 'https://swapi.dev/api/starships/'  # See in the function inside class
    # how it has been set
    assert get_starships_response.request.params == {'page': page}  # See in the function inside class how it has been
    # set
    assert get_starships_response.status_code == status_code_mock
    assert isinstance(get_starships_response.response['results'], list)


def test_get_starship_http_error(requests_mock):
    """ Test Error raise if status code not between 200 and 298 """

    # Mock set up
    requests_mock.get('https://swapi.dev/api/starships/', status_code=404, json={'detail': 'Page not found'})

    # Expect an exceptio to be raised using WITH command
    with pytest.raises(HttpRequestErrors):
        swapi_api_consumer = SwapiApiConsumer()
        page = 100
        get_starships_response = swapi_api_consumer.get_starships(page=page)
