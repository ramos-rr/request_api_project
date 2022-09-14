from cerberus import Validator


def get_pagination_validator(request: any):
    """Pagination validator"""
    querry_param_validator = Validator({
        'page': {'type': 'string', 'allowed': ['1', '2', '3', '4'], 'required': True},
    })

    response = querry_param_validator.validate(request.query_params)
    if not response:
        raise Exception(querry_param_validator.errors)

    print(response)
