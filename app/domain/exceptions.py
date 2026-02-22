class EmailInvalidError(ValueError):
    def __init__(self, email_str: str) -> None:
        self.email_str = email_str
        super().__init__("Invalid email format")
