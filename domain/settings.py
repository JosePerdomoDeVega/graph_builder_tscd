from functools import lru_cache
from typing import Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="allow"
    )
    # Actual implementation

    graph_builder_implementation: Optional[str] = None
    dictionary_loader_implementation: Optional[str] = None

    aws_region: Optional[str] = None
    aws_bucket_name: Optional[str] = None
    dictionary_file_last_version: Optional[str] = None

    neo4j_uri: Optional[str] = None
    neo4j_user: Optional[str] = None
    neo4j_password: Optional[str] = None

    logfire_token: Optional[str] = None
    environment: Optional[str] = None

    def __init__(self, **data):
        super().__init__(**data)


@lru_cache
def get_settings() -> Settings:
    return Settings()
