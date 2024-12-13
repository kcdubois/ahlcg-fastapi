from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    mongo_host: str = "db"
    mongo_port: int = 27017
    mongo_db: str = "ahlcg"
    mongo_username: str | None = None
    mongo_password: str | None = None


settings = Settings()