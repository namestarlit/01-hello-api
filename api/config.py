from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_ignore_empty=True, extra="ignore"
    )

    IPGEOLOCATION_API_KEY: str
    OPENWEATHER_API_KEY: str


settings = Settings()