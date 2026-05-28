from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    SECRET_KEY: str = "super-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7
    MONGO_URI: str = "mongodb://mongo_admin:password@mongo_db:27017/books?authSource=admin"
    
    class Config:
        env_file = ".env"
        extra = "ignore"

settings = Settings()