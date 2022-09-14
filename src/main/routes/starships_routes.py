from fastapi import APIRouter, Request as RequestFastApi


starships_routes = APIRouter()


@starships_routes.get('/')
def home(request: RequestFastApi):
    """
    Homepage
    """
    return {'message': 'Olá mundo'}


# @starships_routes.get('/api/starships/list/page={page}')
# async def read_item(page: int = 1):
#     return {'page': page}


@starships_routes.get('/api/starships/list')
def get_starships_in_paginator(request: RequestFastApi):
    """
    Get Starship paginator
    """
    print(request.query_params['page'])
    print(request.query_params['ola'])
    return {'Olá': 'Mundo'}
