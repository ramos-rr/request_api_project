import pytest
from .request_climate import ClimateRequest
from climatempo.error import *


def test_request_climate(requests_mock):
    # Mock set up
    staus_code_mock = 200
    requests_mock.get(
        'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=a4272cb245450442724f6d775dfeda2a',
        status_code=staus_code_mock,
        json={'locale': 'BR'}
        )

    request_climate = ClimateRequest()
    climate_response = request_climate.get_weather()
    assert climate_response.status_code == staus_code_mock
    assert climate_response.request.method == 'GET'
    assert climate_response.request.url == \
           'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR'


def test_request_climate_http_error(requests_mock):
    with pytest.raises(HttpRequestErrors):
        # Mock set up
        staus_code_mock = 404
        requests_mock.get(
            'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=a4272cb245450442724f6d775dfeda2a',
            status_code=staus_code_mock,
            json={'detail': 'Page not found'}
        )

        request_climate = ClimateRequest()
        climate_response = request_climate.get_weather()


def test_request_climate_invalid_token_error(requests_mock):
    with pytest.raises(InvalidTokenError):
        # Mock set up
        staus_code_mock = 400
        requests_mock.get(
            'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=a4272cb245450442724f6d775dfeda2a',
            status_code=staus_code_mock,
            json={'detail': 'Invalid token'}
        )

        request_climate = ClimateRequest()
        climate_response = request_climate.get_weather()


def test_request_climate_other_error(requests_mock):
    with pytest.raises(OtherError):
        # Mock set up
        staus_code_mock = 451
        requests_mock.get(
            'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=a4272cb245450442724f6d775dfeda2a',
            status_code=staus_code_mock,
            json={'detail': 'Other error'}
        )

        request_climate = ClimateRequest()
        climate_response = request_climate.get_weather()
