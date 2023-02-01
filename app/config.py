from pydantic import BaseSettings


# this pydantic model is a form of validation to check the env variables
class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    secret_key: str
    algorithum: str
    access_token_expire_minutes: int

    class Config:
        env_file = '.env'

settings = Settings()