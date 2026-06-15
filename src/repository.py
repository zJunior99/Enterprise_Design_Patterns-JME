import sqlite3
from abc import ABC, abstractmethod
from typing import Optional, List
from src.models import User


class UserRepository(ABC):
    @abstractmethod
    def save(self, user: User) -> User:
        pass

    @abstractmethod
    def get_by_id(self, user_id: int) -> Optional[User]:
        pass

    @abstractmethod
    def get_all(self) -> List[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int) -> bool:
        pass


class SQLiteUserRepository(UserRepository):
    def __init__(self, db_path: str = "users.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id    INTEGER PRIMARY KEY AUTOINCREMENT,
                    name  TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE
                )
            """)

    def save(self, user: User) -> User:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "INSERT INTO users (name, email) VALUES (?, ?)",
                (user.name, user.email)
            )
            user.id = cursor.lastrowid
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        with sqlite3.connect(self.db_path) as conn:
            row = conn.execute(
                "SELECT id, name, email FROM users WHERE id = ?",
                (user_id,)
            ).fetchone()
        return User(id=row[0], name=row[1], email=row[2]) if row else None

    def get_all(self) -> List[User]:
        with sqlite3.connect(self.db_path) as conn:
            rows = conn.execute(
                "SELECT id, name, email FROM users"
            ).fetchall()
        return [User(id=r[0], name=r[1], email=r[2]) for r in rows]

    def delete(self, user_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.execute(
                "DELETE FROM users WHERE id = ?", (user_id,)
            )
        return cursor.rowcount > 0


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self._store: dict = {}
        self._next_id: int = 1

    def save(self, user: User) -> User:
        user.id = self._next_id
        self._store[self._next_id] = user
        self._next_id += 1
        return user

    def get_by_id(self, user_id: int) -> Optional[User]:
        return self._store.get(user_id)

    def get_all(self) -> List[User]:
        return list(self._store.values())

    def delete(self, user_id: int) -> bool:
        if user_id in self._store:
            del self._store[user_id]
            return True
        return False