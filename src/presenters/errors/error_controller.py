from typing import Type, Dict
from src.errors import HttpRequestErrors, HttpUnprocessableEntityError


def handle_errors(error: Type[Exception]) -> Dict:
    """
    Handler to check for errors
    :param error: Exception
    :return: Dict with data and status_code
    """
    if isinstance(error, HttpRequestErrors):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code,
        }
    elif isinstance(error, HttpUnprocessableEntityError):
        return {
            "data": {"error": error.message},
            "status_code": error.status_code
        }
    else:
        return {
            "data": {"error": str(error)},
            "status_code": 500
        }
