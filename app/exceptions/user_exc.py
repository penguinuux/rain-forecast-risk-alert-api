from http import HTTPStatus


class UserNotFound(Exception):
    def __init__(
        self,
        message: str = "",
        status_code: int = HTTPStatus.NOT_FOUND,
        *args,
        **kwargs
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {"error": "user not found"}

        self.status_code = status_code
