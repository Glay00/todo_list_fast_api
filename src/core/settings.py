from pydantic_settings import BaseSettings
from dotenv import load_dotenv


class DBConfig(BaseSettings):
    host: str
    port: int
    user: str
    password: str
    name: str

    class Config:
        env_prefix = "DB_"

    @property
    def dsn(self):
        return f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.name}"


class Settings(BaseSettings):
    db: DBConfig


def get_settings():
    load_dotenv()
    return Settings(
        db=DBConfig()
    )
