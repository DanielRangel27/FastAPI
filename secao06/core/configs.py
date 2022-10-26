from typing import List

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configraçoes gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:Pipoca-27@localhost:5432/faculdade'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = 'jKGMzIGWRmj9XrUvAc3QWa7WiKIYxc1A0MY1GDRsQj4'
    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """

    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


    class Config:
        case_sensitive = True

settings = Settings()