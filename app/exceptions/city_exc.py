from http import HTTPStatus


class CityOutOfRangeError(Exception):
    def __init__(
        self,
        expected_type: dict = {},
        received_type: dict = {},
        message: str = "",
        status_code: int = HTTPStatus.BAD_REQUEST,
        *args,
        **kwargs
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {
                "error": "city out of range",
                "expected_type": expected_type,
                "received_type": received_type,
            }

        self.status_code = status_code
