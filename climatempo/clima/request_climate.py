from collections import namedtuple
from climatempo.error import ErrorRaise
from climatempo.http_requests import HttpRequests
from climatempo.interface import WeatherRequestInterface
import requests


class ClimateRequest(WeatherRequestInterface):

    __TOKEN_CLIMATEMPO = 'a4272cb245450442724f6d775dfeda2a'

    def __init__(self):
        self.__get_climate_response = namedtuple(typename='GET_climate', field_names='status_code, request, response')

    def get_weather(self, country='BR', token=__TOKEN_CLIMATEMPO):
        request_raw = requests.Request(
            method='GET',
            url=f'http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/{country}',
            params=f'token={token}'
        )
        response = self._prepare_request(request_raw)
        status_code = response.status_code
        return self.__get_climate_response(status_code=status_code, request=request_raw, response=response.json())

    def _prepare_request(self, request_raw):
        request_prepared = request_raw.prepare()
        response = self._send_http_request(request_prepared)
        return response

    def _send_http_request(self, request_prepared):
        response = HttpRequests.send_http_request(request_prepared)
        self._check_error(response)
        return response

    def _check_error(self, response: any):
        return ErrorRaise.check_error(response)


if __name__ == '__main__':
    climatempo = ClimateRequest()
    climatempo.get_weather(country='BR')
    print(climatempo)
