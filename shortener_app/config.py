"""
This module contains the configuration of the application.

Author: Alex Wendland
"""
# This decorator caches the data.
from functools import lru_cache

# This is a library that allows us to use environment variables.
from pydantic import BaseSettings


class Settings(BaseSettings):
    env_name: str = "Local"
    base_url: str = "http://localhost:8000"
    db_url: str = "sqlite:///./shortener.db"

    class Config:
        env_file = ".env"


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    print(f"Environment: {settings.env_name}")
    return settings
