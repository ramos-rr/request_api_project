"""
DEFINING AN ADAPTOR IS DEFINING A BRIDGE BETWEEN FASTAPI AND A METHOD INSIDE OUR INTERNAL PROGRAM (USERCASE)
THIS ADAPTER WILL BE CALLED BY ROUTES!
"""
from typing import Callable
from fastapi import APIRouter, Request as RequestFastApi


async def request_adapter(request: RequestFastApi, callback: Callable):  # callback:Callable is used to do an action!
    """ FastAPI Adapter"""

    # BODY - Build up the BODY content to Recieve something from webpage OR NOT, to avoid error occurrence
    try:
        body = await request.json()  # AWAIT: to wait a litle bite before continuing the code (Waits for the body)
    except:  # If no BODY is provided, then SET UP a NONE BODY!
        body = None

    # HTTP REQUEST - STRUTURE YOUR REQUEST
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
