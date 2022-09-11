import requests
from decouple import config
from climatempo.error import ErrorRaise
from climatempo.http_requests import HttpRequests
from climatempo.interface import IdRequestInterface


class CityIdRequest(IdRequestInterface):

    __TOKEN_CLIMATEMPO = config('TOKEN_CLIMATEMPO')

    @staticmethod
    def get_id(city: str, uf: str, token=__TOKEN_CLIMATEMPO):
        request_raw = requests.Request(
            method='GET',
            url=f"http://apiadvisor.climatempo.com.br/api/v1/locale/city?name={city.title()}&state={uf.upper()}",
            params=f"token={token}"
        )
        response = CityIdRequest._prepare_request(request_raw, )
        city_id = response.json()[0]['id']
        city_name = response.json()[0]['name']
        city_state = response.json()[0]['state']
        return CityIdRequest._inform_id(city_id)

    @staticmethod
    def _inform_id(city_id):
        return city_id

    @staticmethod
    def _prepare_request(request_raw: any, **kwargs):
        prepared_request = request_raw.prepare()
        response = CityIdRequest._send_http_request(prepared_request, )
        return response

    @staticmethod
    def _send_http_request(request_prepared, **kwargs):
        response = HttpRequests.send_http_request(request_prepared)
        CityIdRequest._check_error(response)
        return response

    @staticmethod
    def _check_error(response: any, **kwargs):
        return ErrorRaise.check_error(response)


if __name__ == '__main__':
    city = CityIdRequest()
    city.get_id('jundiaí', 'sp')

