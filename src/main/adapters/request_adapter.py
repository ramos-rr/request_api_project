from typing import Callable
from fastapi import APIRouter, Request as RequestFastApi


async def request_adapter(request: RequestFastApi, callback: Callable):  # callback:Callable is used to do an action!
    """ FastAPI Adapter"""

    # BODY
    try:
        body = await request.json()
    except:
        body = None

    http_request = {
        'query_params': request.query_params,
        'body': body,
    }

    # HTTP RESPONSE
    try:
        http_response = callback(http_request)
        return http_response
    except:
        print('An error has occurred')
