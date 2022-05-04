from http import HTTPStatus


class CityNotFoundError(Exception):
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
                "error": "city not found",
                "expected_type": expected_type,
                "received_type": received_type,
            }

        self.status_code = status_code


class ZipCodeNotFoundError(Exception):
    def __init__(
        self,
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
                "error": "zip code not found",
            }

        self.status_code = status_code


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
