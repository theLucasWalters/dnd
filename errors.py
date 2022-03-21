class InvalidSpecies(BaseException):
    def __init__(self, error):
        self.error = error

    def __repr__(self) -> str:
        return f"Invalid species: {self.error}"

class InvalidAlignment(BaseException):
    def __init__(self, error):
        self.error = error

    def __repr__(self) -> str:
        return f"Invalid Alignment: {self.error}"
