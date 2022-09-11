class HttpRequestErrors(Exception):
    def __init__(self, message: str, status_code: int) -> None:
        """
        HTTP error
        :param message: Message to show user when this error is raised
        :param status_code: Status code related to this error
        """
        super().__init__(message)
        self.message = message
        self.status_code = status_code
