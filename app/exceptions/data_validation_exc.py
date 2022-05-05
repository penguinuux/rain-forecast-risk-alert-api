from http import HTTPStatus


class InvalidFormat(Exception):
    def __init__(
        self,
        key: str = "",
        expected_format: str = "",
        received_format: str = "",
        status_code: int = HTTPStatus.BAD_REQUEST,
        message: str = "",
        *args,
        **kwargs,
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {
                "error": f"invalid {key} format",
                "expected_format": expected_format,
                "received_format": received_format,
            }

        self.status_code = status_code
