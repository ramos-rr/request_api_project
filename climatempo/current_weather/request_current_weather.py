from climatempo.http_requests import HttpRequests
from climatempo.interface import WeatherRequestInterface
from climatempo.city_id import CityIdRequest
from climatempo.error import ErrorRaise
from decouple import config
import requests


class CurrentWeatherRequest(WeatherRequestInterface):

    __TOKEN_CLIMATEMPO = config('TOKEN_CLIMATEMPO')
    __CITY = config('CITY')
    __STATE = config('STATE')

    @staticmethod
    def get_weather(city=__CITY, state=__STATE, token=__TOKEN_CLIMATEMPO):
        city_id = CityIdRequest.get_id(city=city, uf=state)
        # CurrentWeatherRequest._put_location(city_id)
        request_raw = requests.Request(
            method='GET',
            url=f"http://apiadvisor.climatempo.com.br/api/v1/weather/locale/{city_id}/current",
            params=f"token={token}"
        )
        response = CurrentWeatherRequest._prepare_request(request_raw)
        print(f'Imprimindo o clima de {response.json()["name"]} / {response.json()["state"]}:')
        for chave, valor in response.json()['data'].items():
            print(chave.title(), valor, sep=': ')

    @staticmethod
    def _prepare_request(request_raw: any):
        request_prepared = request_raw.prepare()
        response = CurrentWeatherRequest._send_http_request(request_prepared)
        return response

    @staticmethod
    def _send_http_request(request_prepared):
        response = HttpRequests.send_http_request(request_prepared)
        CurrentWeatherRequest._check_error(response)
        return response

    @staticmethod
    def _check_error(response: any, **kwargs):
        return ErrorRaise.check_error(response)

    # @staticmethod
    # def _put_location(city_id, token=__TOKEN_CLIMATEMPO):
    #     """
    #     Method necessary beforerand to get authorization from CLIMATEMPO to return data from the desired city
    #     :param city_id: City's ID
    #     :param token: Climatempo token
    #     :return: None
    #     """
    #     url = f'http://apiadvisor.climatempo.com.br/api-manager/user-token/{token}/locales'
    #     headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    #     payload = f"localeId[]={city_id}"
    #     response_put = requests.request('PUT', url=url, headers=headers, data=payload)
    #     CurrentWeatherRequest._check_error(response_put)
    #     return None


if __name__ == '__main__':
    temp = CurrentWeatherRequest()
    temp.get_weather()

