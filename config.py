import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "fallback-secret")

    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    EXPORT_DIR = os.path.join(BASE_DIR, "exports")
