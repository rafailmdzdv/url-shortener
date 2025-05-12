from typing import Protocol


class NewUser(Protocol):
    """Протокол нового пользователя."""

    async def create(self) -> None:
        """Создать нового пользователя."""
