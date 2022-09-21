from src.errors import HttpUnprocessableEntityError
from cerberus import Validator


def get_pagination_validator(request: any):
    """Pagination validator"""

    # CREATING A VALIDATION SCHEMA:
    querry_param_validator = Validator({
        'page': {'type': 'string', 'allowed': ['1', '2', '3', '4'], 'required': True},
    })

    # .validade() is a buit in function inside CERBERUS that returns TRUE if all conditions match with the request
    response = querry_param_validator.validate(request.query_params)
    if not response:
        print(f'Validation == {response}')
        print(f'-> Params got == {request.query_params}' if len(request.query_params) != 0 else 'Params got == "empty"')
        print(f"--> {querry_param_validator.errors}")
        raise HttpUnprocessableEntityError(message=querry_param_validator.errors)

    else:
        print(f'Validation == {response}')
        return response
