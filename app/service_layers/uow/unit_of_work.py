from abc import ABC, abstractmethod
from app.repositories.user_repository import (
    InMemoryUserRepository,
    PostgresUserRepository,
)


class UnitOfWork(ABC):
    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @abstractmethod
    def commit(self):
        pass

    @abstractmethod
    def rollback(self):
        pass

    @property
    @abstractmethod
    def user_repository(self):
        pass


class InMemoryUnitOfWork(UnitOfWork):
    def __init__(self):
        self._user_repository = InMemoryUserRepository()

    def commit(self):
        pass

    def rollback(self):
        pass

    @property
    def user_repository(self):
        return self._user_repository


class PostgresUnitOfWork(UnitOfWork):
    def __init__(self, connection):
        self.connection = connection
        self._user_repository = PostgresUserRepository(connection)

    def __enter__(self):
        return self

    def commit(self):
        self.connection.commit()

    def rollback(self):
        self.connection.rollback()

    @property
    def user_repository(self):
        return self._user_repository
