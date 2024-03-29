from http import HTTPStatus


class CityNotFoundError(Exception):
    def __init__(
        self,
        expected_type: dict = {},
        received_type: dict = {},
        message: str = "",
        status_code: int = HTTPStatus.NOT_FOUND,
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


class CityOutOfRangeError(Exception):
    def __init__(
        self,
        cities_coverage: dict = {},
        received_city: dict = {},
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
                "error": "city out of coverage",
                "received_city": received_city,
                "cities_coverage": cities_coverage,
            }

        self.status_code = status_code


class ZipCodeNotFoundError(Exception):
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
            self.message = {
                "error": "zip code not found",
            }

        self.status_code = status_code


class InvalidZipCodeFormatError(Exception):
    def __init__(
        self,
        zip_code: str,
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
                "error": "invalid zip code format",
                "expected_type": "99999-999",
                "received_type": zip_code,
            }

        self.status_code = status_code
