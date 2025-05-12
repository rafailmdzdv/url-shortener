from typing import Protocol


class User(Protocol):
    """Пользователь (интерфейс)."""

    async def id(self) -> int:
        """Идентификатор пользователя."""
