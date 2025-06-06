from aiogram import types
from aiogram.dispatcher.middlewares import BaseMiddleware
from utils.cache import cache

class ThrottlingMiddleware(BaseMiddleware):
    async def on_process_message(self, message: types.Message, data: dict):
        if await cache.exists(f"throttle:{message.from_user.id}"):
            raise CancelHandler()
        await cache.set(f"throttle:{message.from_user.id}", "1", expire=2)
