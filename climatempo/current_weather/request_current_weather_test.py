from climatempo.city_id.test.request_city_id import mock_city_id
from climatempo.current_weather.request_current_weather import CurrentWeatherRequest
from decouple import config

from climatempo.current_weather.test.request_current_weather import CurrentWeatherRequestSpy


def test_get_weather(requests_mock):
    # mock set up for CITY_ID
    requests_mock.get(
        f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name=Jundia%C3%AD&state=SP&token={config('TOKEN_CLIMATEMPO')}",
        json=mock_city_id()
    )
    # mockset up for current weather
    requests_mock.get(
        f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3877/current?token={config("TOKEN_CLIMATEMPO")}',
        json=CurrentWeatherRequestSpy.get_weather()
    )
    weather = CurrentWeatherRequest()
    response = weather.get_weather()
    assert isinstance(response['id'], int)
    assert isinstance(response['data'], dict)
