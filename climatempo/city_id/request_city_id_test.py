import pytest
from climatempo.city_id import CityIdRequest
from decouple import config
from climatempo.error import InvalidTokenError, HttpRequestErrors, OtherError
from climatempo.error.no_data_found_error import NoDataFoundError


def test_request_city_id(requests_mock):
    # mock set up
    requests_mock.get(
        f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=Jundia%C3%AD&state=SP&token={config("TOKEN_CLIMATEMPO")}',
        json=[{'id': 1234, 'name': 'Jundiaí', 'state': 'SP'}],
    )
    city = CityIdRequest()
    city_id_response = city.get_id('Jundiaí', 'SP')
    assert isinstance(city_id_response, int)


def test_request_city_id_invalid_token_error(requests_mock):
    # mock set up
    with pytest.raises(InvalidTokenError):
        requests_mock.get(
            f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=Jundia%C3%AD&state=SP&token={config("TOKEN_CLIMATEMPO")}',
            status_code=400,
            json={'detail': 'Invalid token'},
        )
        city = CityIdRequest()
        city_id_response = city.get_id('Jundiaí', 'SP')


def test_request_city_id_http_error(requests_mock):
    # mock set up
    with pytest.raises(HttpRequestErrors):
        requests_mock.get(
            f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=Jundia%C3%AD&state=SP&token={config("TOKEN_CLIMATEMPO")}',
            status_code=404,
            json={'detail': 'Page not found'},
        )
        city = CityIdRequest()
        city_id_response = city.get_id('Jundiaí', 'SP')


def test_request_city_other_error(requests_mock):
    # mock set up
    with pytest.raises(OtherError):
        requests_mock.get(
            f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=Jundia%C3%AD&state=SP&token={config("TOKEN_CLIMATEMPO")}',
            status_code=451,
            json={'detail': 'Other error'},
        )
        city = CityIdRequest()
        city_id_response = city.get_id('Jundiaí', 'SP')


def test_request_city_id_nodatafound_error(requests_mock):
    with pytest.raises(NoDataFoundError):
        requests_mock.get(
            f'http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=Jundia%C3%AD&state=AM&token={config("TOKEN_CLIMATEMPO")}',
            status_code=200,
            text='[]',
        )
        city = CityIdRequest()
        city_id_response = city.get_id('Jundiaí', 'AM')
