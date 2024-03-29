from typing import Optional

from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков QRKot'
    app_description: str = 'Сбор пожертвований в целевые проекты на нужды хвостатых'
    database_url: str = 'sqlite+aiosqlite:///./qpkot.db'
    secret: str = 'SECRET'

    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None
    email: Optional[str] = None

    v_sheets: str = 'v4'
    v_drive: str = 'v3'
    list_title: str = 'Лист1'
    row: int = 100
    column: int = 10

    class Config:
        env_file = '.env'


settings = Settings()
