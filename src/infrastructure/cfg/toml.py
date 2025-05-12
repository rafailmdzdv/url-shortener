import tomllib
from dataclasses import dataclass, field
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
        toml = tomllib.load(self.file_path.open('rb'))
        return toml['storage']['postgres_dsn']


@final
@dataclass(frozen=True)
class CachedTomlSettings(Settings):
    """Настройки проекта из `.toml` файла с примитивным кэшированием."""

    settings: Settings
    _cache: dict[str, str] = field(init=False, default_factory=dict)

    @override
    async def postgres_dsn(self) -> str:
        if not self._cache.get('postgres_dsn'):
            self._cache['postgres_dsn'] = await self.settings.postgres_dsn()
        return self._cache['postgres_dsn']
