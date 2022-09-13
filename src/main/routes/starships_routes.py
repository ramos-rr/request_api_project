from fastapi import APIRouter, Request as RequestFastApi


starships_routes = APIRouter()


@starships_routes.get('/')
def home(request: RequestFastApi):
    """
    Homepage
    """
    print(request.query_params)
    return 'Olá Mundo'


@starships_routes.get('/api/starships/list')
def get_starships_in_paginator(request: RequestFastApi):
    """
    Get Starship paginator
    """
    return {'Olá': 'Mundo'}