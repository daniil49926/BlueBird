import os
from typing import Optional

from pydantic import BaseSettings

from core.utils.load_env import load_environ

_BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_environ(_BASE_DIR)


def get_var(var_name: str) -> Optional[str | int]:
    return os.environ.get(var_name)


class __Settings(BaseSettings):
    HOST: str = get_var("APPLICATION_HOST")
    PORT: int = get_var("APPLICATION_PORT")

    RELOAD: bool = True
    BASE_DIR: str = _BASE_DIR

    PG_HOST: str = "pg_db"
    PG_PORT: int = get_var("PG_PORT_HOST")
    PG_USER: str = get_var("PG_USER")
    PG_PASSWORD: str = get_var("PG_PASSWORD")
    PG_MAIN_DB: str = get_var("PG_MAIN_DB")
    PG_DSN = f"{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_MAIN_DB}"

    MAX_ATTEMPTS_TO_CONN_TO_PG: int = 5

    TESTING: bool = get_var("TESTING")


settings = __Settings()
