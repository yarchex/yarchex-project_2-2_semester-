import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    ALIPAY_API_KEY = os.getenv("ALIPAY_API_KEY")
    RAKETA_API_KEY = os.getenv("RAKETA_API_KEY")
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    ADMIN_IDS = list(map(int, os.getenv("ADMIN_IDS", "").split(",")))

settings = Settings()
