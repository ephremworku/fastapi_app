class Settings:
    PROJECT_NAME: str = "FastAPI Clean Architecture Example"
    VERSION: str = "1.0.0"
    SQLALCHEMY_DATABASE_URL: str = "sqlite:///./users.db"

settings = Settings()
