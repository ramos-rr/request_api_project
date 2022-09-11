from abc import abstractmethod, ABC
from decouple import config


class WeatherRequestInterface(ABC):

    __TOKEN_CLIMATEMPO = config('TOKEN_CLIMATEMPO')

    @staticmethod
    def get_weather() -> None:
        """ Function to get specific wheather information """
        raise NotImplementedError

    @staticmethod
    def _prepare_request(request_raw: any):
        """ Function to prepare request in the right format to be sent"""
        raise NotImplementedError

    @staticmethod
    def _send_http_request(request_prepared):
        """ Function to send HTTP request """
        raise NotImplementedError

    @staticmethod
    def _check_error(self, response: any):
        """Function to check up if there is any error in the request"""
        raise NotImplementedError


class IdRequestInterface(ABC):

    __TOKEN_CLIMATEMPO = NotImplementedError

    @abstractmethod
    def get_id(self, city, token) -> None:
        """ Function to get specific wheather information """
        raise NotImplementedError

    @abstractmethod
    def _inform_id(self, city_id):
        """ Function to return City's ID"""
        raise NotImplementedError

    @abstractmethod
    def _prepare_request(self, request_raw: any):
        """ Function to prepare request in the right format to be sent"""
        raise NotImplementedError

    @abstractmethod
    def _send_http_request(self, request_prepared):
        """ Function to send HTTP request """
        raise NotImplementedError

    @abstractmethod
    def _check_error(self, response: any):
        """Function to check up if there is any error in the request"""
        raise NotImplementedError
