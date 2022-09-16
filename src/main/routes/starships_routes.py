from fastapi import APIRouter, Request as RequestFastApi
from src.validators.get_starships_in_pagination_validator import get_pagination_validator
from src.main.adapters.request_adapter import request_adapter


starships_routes = APIRouter()


@starships_routes.get('/')
def home(request: RequestFastApi):
    """
    Homepage
    """
    return {'message': 'Olá mundo'}


@starships_routes.get('/api/starships/list')
# async def means that some requests will have to wait the response, that it can't be so fast otherwise is going to fail
async def get_starships_in_pagination(request: RequestFastApi):
    """
    Get Starship paginator
    """
    get_pagination_validator(request)
    await request_adapter(request, print)

    return {'Olá': 'Mundo'}
