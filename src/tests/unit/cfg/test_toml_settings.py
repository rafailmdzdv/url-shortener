from aiopath import AsyncPath

from infrastructure.cfg.toml import TomlSettings


async def test_toml_settings() -> None:
    settings = TomlSettings(AsyncPath(__file__).parent / 'test.config.toml')

    postgres_dsn = await settings.postgres_dsn()

    assert postgres_dsn == 'protocol://u:p@i:p/db'
