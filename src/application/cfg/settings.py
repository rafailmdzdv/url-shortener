from typing import Protocol


class Settings(Protocol):
    """Настройки проекта."""

    async def postgres_dsn(self) -> str:
        """Connection-url для PostgreSQL."""
