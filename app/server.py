from loguru import logger
from app.config.config import ENV
from fastapi import FastAPI
from app.initializers import init

app = FastAPI(logger=logger)

init(app)

logger.info(f"🚀 Service was initialized! 🛸 (env: {ENV})")

