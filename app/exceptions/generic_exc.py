from http import HTTPStatus


class InvalidTypeError(Exception):
    def __init__(
        self,
        expected_type: dict = {},
        received_type: dict = {},
        message: str = "",
        status_code: int = HTTPStatus.BAD_REQUEST,
        *args,
        **kwargs,
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {
                "error": "invalid type",
                "expected_type": expected_type,
                "received_type": received_type,
            }

        self.status_code = status_code


class MissingKeysError(Exception):
    def __init__(
        self,
        expected_keys: dict = {},
        missing_keys: dict = {},
        message: str = "",
        status_code: int = HTTPStatus.BAD_REQUEST,
        *args,
        **kwargs,
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {
                "error": "missing keys",
                "expected_keys": expected_keys,
                "missing_keys": missing_keys,
            }

        self.status_code = status_code


class InvalidKeysError(Exception):
    def __init__(
        self,
        expected_keys: dict = {},
        invalid_keys: dict = {},
        message: str = "",
        status_code: int = HTTPStatus.BAD_REQUEST,
        *args,
        **kwargs,
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {
                "error": "invalid keys",
                "expected_keys": expected_keys,
                "invalid_keys": invalid_keys,
            }

        self.status_code = status_code


class UniqueKeyError(Exception):
    def __init__(
        self,
        key: str = "",
        message: str = "",
        status_code: int = HTTPStatus.CONFLICT,
        *args,
        **kwargs,
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {"error": f"unique {key} error"}

        self.status_code = status_code


class InvalidCredentialsError(Exception):
    def __init__(
        self,
        message: str = "",
        status_code: int = HTTPStatus.BAD_REQUEST,
        *args,
        **kwargs,
    ):
        super().__init__(args, kwargs)
        if message:
            self.message = message
        else:
            self.message = {"error": "invalid credentials"}

        self.status_code = status_code
