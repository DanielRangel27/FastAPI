from pydantic import BaseSettings


class Settings(BaseSettings):
    """
    Configraçoes gerais usadas na aplicação
    """
    API_V1_STR: str = '/api/v1'
    DB_URL: str = 'postgresql+asyncpg://postgres:Pipoca-27@localhost:5432/faculdade'


    class Config:
        case_sensitive = True

settings = Settings()