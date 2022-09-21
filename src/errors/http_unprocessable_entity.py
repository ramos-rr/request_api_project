class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        """
        HTTP Unprocessable error
        :param message: Message to show user when this error is raised
        """
        super().__init__(message)
        self.name = 'Unprocessable entity'
        self.message = message
        self.status_code = 422
