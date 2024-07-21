from app.domain.model.user import User
from app.domain.services.email_service import EmailValidationService
from app.service_layers.uow.unit_of_work import UnitOfWork


class UserService:
    def __init__(self, uow: UnitOfWork):
        self.uow = uow

    def register_user(self, user_id: str, name: str, email: str) -> None:
        with self.uow:
            existing_user = self.uow.user_repository.find_by_user_id(user_id)
            if existing_user:
                raise ValueError("User with this ID already exists")

            if not EmailValidationService.is_valid_email(email):
                raise ValueError("Invalid email domain")

            new_user = User(user_id, name, email)
            self.uow.user_repository.save(new_user)
            self.uow.commit()
