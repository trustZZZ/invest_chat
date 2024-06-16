from dotenv import load_dotenv
from pydantic import ConfigDict
from pydantic_settings import BaseSettings

load_dotenv()


class Settings(BaseSettings):
    DB_HOST: str | None = None
    DB_PORT: int | None = None
    DB_USER: str | None = None
    DB_PASS: str | None = None
    DB_NAME: str | None = None
    URL: str | None = None
    SECRET_KEY: str | None = None
    ALGORITHM: str | None = None

    model_config = ConfigDict(extra='allow')



settings = Settings()
