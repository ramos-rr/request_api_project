import pytest
from .swapi_api_consumer import SwapiApiConsumer
from src.errors import HttpRequestErrors, HttpUnprocessableEntityError


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


def test_get_starship_http_unprocessable_entity_error(requests_mock):
    """ Test Error raise if status code not between 200 and 298 """

    # Mock set up
    requests_mock.get('https://swapi.dev/api/starships/', status_code=422, json={'detail': 'Unprocessable entity error'})

    # Expect an exceptio to be raised using WITH command
    with pytest.raises(HttpUnprocessableEntityError):
        swapi_api_consumer = SwapiApiConsumer()
        page = 1
        get_starships_response = swapi_api_consumer.get_starships(page=page)


def test_get_starship_information(requests_mock):
    """Test a HTTP response for individual starship"""
    # set up mock
    starship_id = 9
    requests_mock.get(f'https://swapi.dev/api/starships/{starship_id}/', status_code=200, json={'name': 'some',
                                                                                                'model': 'thing',
                                                                                                'MGTL': '123'})
    swapi_api_consumer = SwapiApiConsumer()
    response = swapi_api_consumer.get_starship_information(starship_id)
    assert response.request.method == 'GET'
    assert response.request.url == f'https://swapi.dev/api/starships/{starship_id}/'
    assert response.status_code == 200


def test_get_starship_information_http_error(requests_mock):
    """Test HTTP response for individual starship as ERROR """
    # set up mock
    with pytest.raises(HttpUnprocessableEntityError):
        starship_id = 9
        requests_mock.get(f'https://swapi.dev/api/starships/{starship_id}/',
                          status_code=422,
                          json={'detail': 'Unprocessable entity error'})
        swapi_api_consumer = SwapiApiConsumer()
        response = swapi_api_consumer.get_starship_information(starship_id)


def test_get_starship_information_http_unprocessable_entity_error(requests_mock):
    """Test HTTP Unprocessable ERROR """
    # set up mock
    with pytest.raises(HttpRequestErrors):
        starship_id = 9
        requests_mock.get(f'https://swapi.dev/api/starships/{starship_id}/',
                          status_code=404,
                          json={'detail': 'Page not found'})
        swapi_api_consumer = SwapiApiConsumer()
        response = swapi_api_consumer.get_starship_information(starship_id)