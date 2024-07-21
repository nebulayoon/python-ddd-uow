from abc import ABC, abstractmethod
from app.domain.model.user import User
import psycopg


class UserRepository(ABC):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> User:
        pass

    @abstractmethod
    def save(self, user: User) -> None:
        pass


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = {}

    def find_by_user_id(self, user_id: str) -> User:
        return self.users.get(user_id)

    def save(self, user: User) -> None:
        self.users[user.user_id] = user


class PostgresUserRepository(UserRepository):
    def __init__(self, connection):
        self.connection = connection

    def find_by_user_id(self, user_id: str) -> User:
        with self.connection.cursor() as cursor:
            cursor.execute("SELECT * FROM users WHERE user_id = %s", (user_id,))
            row = cursor.fetchone()
            if row:
                return User(row["user_id"], row["name"], row["email"])
            return None

    def save(self, user: User) -> None:
        with self.connection.cursor() as cursor:
            cursor.execute(
                "INSERT INTO users (user_id, name, email) VALUES (%s, %s, %s) ON CONFLICT (user_id) DO NOTHING",
                (user.user_id, user.name, user.email),
            )
            self.connection.commit()
