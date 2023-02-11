from pydantic import BaseSettings
from functools import lru_cache
import os

@lru_cache
def get_env_filename():
    runtime_env = os.getenv("ENV")
    return f".env.{runtime_env}" if runtime_env else ".env"


class Environment(BaseSettings):
    DATABASE_HOSTNAME : str
    DATABASE_NAME : str
    DATABASE_PASSWORD : str
    DATABASE_PORT : str
    DATABASE_USERNAME : str
    DATABASE_DIALECT : str
    DEBUG_MODE : bool

    class Config:
        env_file = get_env_filename()
        env_file_encoding = "utf-8"


@lru_cache
def get_environment_variables():
    return Environment()