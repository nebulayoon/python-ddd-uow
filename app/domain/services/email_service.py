class EmailValidationService:
    @staticmethod
    def is_valid_email(email: str) -> bool:
        return email.endswith("@example.com")
