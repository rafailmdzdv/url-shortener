import tomllib
from dataclasses import dataclass
from typing import final, override

from aiopath import AsyncPath

from application.cfg.settings import Settings


@final
@dataclass(frozen=True)
class TomlSettings(Settings):
    """Настройки проекта из `.toml` файла."""

    file_path: AsyncPath

    @override
    async def postgres_dsn(self) -> str:
        toml = tomllib.load(await self.file_path.open('rb'))
        return toml['storage']['postgres_dsn']
