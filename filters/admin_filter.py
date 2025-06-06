from aiogram.dispatcher.filters import BoundFilter
from aiogram import types
from config.settings import settings

class IsAdminFilter(BoundFilter):
    async def check(self, message: types.Message):
        return message.from_user.id in settings.ADMIN_IDS
