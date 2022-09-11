from climatempo.error import *
from climatempo.error.no_data_found_error import NoDataFoundError


class ErrorRaise:
    """
    Class instantiated to check if there's any error and return positive or negative
    """

    @classmethod
    def check_error(cls, response):
        """
        Funtion to check if there's an error by checking up the response.status_code.
        :param response: Response coming from HTTP request.
        :return: If no error has been found, return Response back. If there's an error, return raises the right error
        """
        if 299 >= response.status_code >= 200:
            pass
        elif response.status_code == 400:
            raise InvalidTokenError(message=response.json()['detail'], status_code=response.status_code)
        elif response.status_code == 404:
            raise HttpRequestErrors(message=response.reason, status_code=response.status_code)
        else:
            raise OtherError(message=response.text, status_code=response.status_code)

        try:
            if len(response.json()) == 0:
                raise NoDataFoundError(message='No data was found')
            else:
                pass
        except:
            pass
        else:
            return None


