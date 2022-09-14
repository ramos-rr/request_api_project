from fastapi import APIRouter, Request as RequestFastApi
from src.validators.get_starships_in_pagination_validator import get_pagination_validator


starships_routes = APIRouter()


@starships_routes.get('/')
def home(request: RequestFastApi):
    """
    Homepage
    """
    return {'message': 'Olá mundo'}


@starships_routes.get('/api/starships/list')
def get_starships_in_pagination(request: RequestFastApi):
    """
    Get Starship paginator
    """
    get_pagination_validator(request)

    return {'Olá': 'Mundo'}
