import requests
from typing import Type
from requests import Request
from collections import namedtuple


class SwapiApiConsumer:

    def __init__(self):
        self.get_starships_response = namedtuple(typename='GET_response', field_names='status_code, request, response')

    def get_starships(self, page: int) -> any:
        """
        Funtion to get an HTTP from StarWars Starships.
        :param page: int: Page number desired.
        :return: Full HTTP page in JSON format.
        """
        # Below, the simplest way to use resquest = Method GET Directly
        # params = {'page': page}
        # response = requests.get('https://swapi.dev/api/starships/', params=params)

        # Below, a more sophisticated method to use GET
        req_row = requests.Request(
            method='GET',
            url='https://swapi.dev/api/starships/',
            params={'page': page}

        )
        req_prepared = req_row.prepare()  # function prepare() comes with requests
        response = self.__send_http_requests(req_prepared)

        return self.get_starships_response(
            status_code=response.status_code,
            request=req_row,
            response=response.json()
        )

    @classmethod
    def __send_http_requests(cls, req_prepared: Type[Request]) -> any:
        """
        Function to send HTTP to API in the right format.
        :param req_prepared: address informed by the function get_startship above
        :return: HTTP in the right format
        """
        http_session = requests.Session()
        response = http_session.send(req_prepared)
        return response
