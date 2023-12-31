from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    app_title: str = 'Благотворительный фонд поддержки котиков'
    app_description: str = 'Фонд собирает пожертвования на различные целевые проекты'
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'secret'
    first_superuser_email: Optional[EmailStr] = None
    first_superuser_password: Optional[str] = None
    password_min_len: int = 3

    class Config:
        env_file = '.env'


settings = Settings()
