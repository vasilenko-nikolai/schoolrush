class PersonAlreadyExistsError(Exception):
    def __init__(self, exists_field: str, expected: str) -> None:
        self.exists_field = exists_field
        self.expected = expected
        super().__init__(f"Person with {exists_field}={expected} already exists")
