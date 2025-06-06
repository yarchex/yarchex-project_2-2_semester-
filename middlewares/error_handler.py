from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.logger import logger

class ErrorHandlerMiddleware(BaseMiddleware):
    async def on_process_error(self, update: types.Update, error: Exception):
        logger.error(f"Update {update} caused error: {error}")
        if isinstance(update, types.Message):
            await update.answer("⚠️ Произошла ошибка. Попробуйте позже.")
