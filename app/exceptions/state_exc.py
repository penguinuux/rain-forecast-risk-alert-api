class StateNotFoundError(Exception):
    def __init__(self) -> None:
        self.message = {"error": "State not found!"}
        super().__init__(self.message)
