import requests
from typing import Type  # Tuple, Dict
from requests import Request, Response
from collections import namedtuple
from src.data.interfaces.swapi_api_consumer import SwapiApiConsumerInterface
from src.errors import HttpRequestErrors


class SwapiApiConsumer(SwapiApiConsumerInterface):

    def __init__(self):
        self.get_starships_response = namedtuple(typename='GET_Starships', field_names='status_code, request, response')

    def get_starships(self, page: int) -> 'GET_Starships':
        """
        Funtion to get an HTTP from StarWars Starships.
        :param page: int: Page number desired.
        :return: Full HTTP page in JSON format.
        """
        # Below, the simplest way to use resquest = Method GET Directly
        # params = {'page': page}
        # response = requests.get('https://swapi.dev/api/starships/', params=params)

        # Below, a more sophisticated method to use GET
        req_raw = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={'page': page},
        )
        req_prepared = req_raw.prepare()  # function prepare() comes with requests
        response = self.__send_http_requests(req_prepared)
        status_code = response.status_code

        if 200 <= status_code <= 299:
            return self.get_starships_response(
                status_code=status_code,
                request=req_raw,
                response=response.json()
            )
        else:
            raise HttpRequestErrors(
                message=response.json()["detail"], status_code=status_code
            )

    @classmethod
    def __send_http_requests(cls, req_prepared: Type[Request]) -> Response:
        """
        Method to send HTTP to API in the right format.
        :param req_prepared: address informed by the function get_startship above
        :return: HTTP in the right format
        """
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
